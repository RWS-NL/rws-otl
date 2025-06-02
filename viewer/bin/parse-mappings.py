#!/usr/bin/env python3

import argparse
import csv
import json
import os

OTL_URI_PREFIX = "https://data.rws.nl/def/otl/"
OTL_URI_PREFIX_LEN = len(OTL_URI_PREFIX)


def main():
    args = parse_args()

    # Hier houden we de mapping-data bij. De structuur is als volgt:
    # {
    #    "Naam van OTL-concept": {
    #      "Naam van OTL-kenmerk": {
    #        "Naam van BMS": {
    #           "datatype-bms": "...",
    #           "datatype-otl": "..."
    #        }
    #      }
    #    }
    # }
    mapping_data = {}

    for file in os.listdir(args["mapping_root"]):
        if file.endswith(".csv"):
            bms = file[:-4]
            bms_row_count = 0

            with open(os.path.join(args["mapping_root"], file), newline="") as source_file:
                for row in csv.reader(source_file, delimiter=";", quotechar='"'):
                    # Het 3e veld bevat potentieel een OTL-concept
                    if row[2].startswith(OTL_URI_PREFIX):
                        concept = row[2][OTL_URI_PREFIX_LEN:]
                    else:
                        # Zo niet, sla de regel dan over
                        continue

                    # Het 7e veld bevat potentieel een OTL-kenmerk
                    if row[6].startswith(OTL_URI_PREFIX):
                        kenmerk = row[6][OTL_URI_PREFIX_LEN:]
                    else:
                        # Zo niet, sla de regel dan over
                        continue

                    # Veld 4 bevat de naam uit het BMS
                    name_bms = row[3]

                    # Velden 12 en 13 bevatten de BMS- en OTL-datatypen
                    datatype_bms = row[11]
                    datatype_otl = row[12]

                    # Voeg toe aan dataset
                    if concept not in mapping_data:
                        mapping_data[concept] = {}
                    if kenmerk not in mapping_data[concept]:
                        mapping_data[concept][kenmerk] = {}
                    if bms in mapping_data[concept][kenmerk]:
                        print(
                            f"Bronsysteem '{bms}': Concept '{concept}', Kenmerk '{kenmerk}' komt meerdere keren voor in mapping."
                        )
                        continue
                    mapping_data[concept][kenmerk][bms] = {"datatype-bms": datatype_bms, "datatype-otl": datatype_otl, "name-bms": name_bms}

                    bms_row_count += 1

            print(f"Bronsysteem '{bms}': {bms_row_count} regels verwerkt")

    with open(args["output_file"], "w", encoding="utf-8") as output_file:
        json.dump(mapping_data, output_file)


def parse_args():
    parser = argparse.ArgumentParser(description="Parse mappings.")
    parser.add_argument(
        "mapping_root",
        help="Pad naar de directory waar de mapping rules in CSV-vorm beschikbaar zijn.",
    )
    parser.add_argument(
        "output_file",
        help="Pad waar de geparsete dataset opgeslagen moet worden als JSON.",
    )
    parser.add_argument(
        "-v", "--verbose", help="Geef extra output ter ondersteuning van ontwikkelen of debuggen.", action="store_true"
    )
    args = parser.parse_args()

    return {
        "mapping_root": args.mapping_root,
        "output_file": args.output_file,
        "verbose": args.verbose,
    }


if __name__ == "__main__":
    main()
