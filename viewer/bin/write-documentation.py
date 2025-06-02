#!/usr/bin/env python3

# Verwerk OTL UTD tot een documentatie in de vorm van een set Markdown-bestanden.

from rdflib import ConjunctiveGraph
from urllib.parse import quote, unquote
import time
import argparse
import os
import json
import sys

def main():
    """
    Verwerk OTL tot een documentatie in de vorm van een set Markdown-bestanden.
    """
    start_time = time.time()
    args = parse_args()

    files = [
        f'{args["root"]}/ontology/def/otl/graaf-kennismodel.trig',
        f'{args["root"]}/ontology/def/linksets/graaf-otl-utd-linkset.trig',
        f'{args["root"]}/ontology/def/utd/graaf-kennismodel-utd.trig',
        f'{args["root"]}/ontology/def/otl/graaf-informatiemodel.trig',
    ]

    print("Reading")
    print("...Initials")

    # Create an empty ConjunctiveGraph
    ds = ConjunctiveGraph()

    # Parse multiple .trig files into the graph

    for file in files:
        ds.parse(file, format="trig")

    query = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT ?resource ?label ?definition ?broader
        WHERE {
            GRAPH <https://data.rws.nl/def/otl/graaf-kennismodel> {
            ?resource a skos:Concept ;
                    skos:prefLabel ?label ;
                    skos:definition ?definition ;
                    skos:broaderTransitive ?broader .
        }
        }
    ORDER BY ASC (?label)
    """

    results_array = []

    results = ds.query(query)

    for row in results:
        result_dict = {
            "resource": row["resource"],
            "label": row["label"],
            "definition": row["definition"],
            "broader": row["broader"],
        }
        results_array.append(result_dict)

    distinct_initials = ""
    prev_initial = ""
    for entry in results_array:
        entry_str = entry["label"]
        initial = entry_str[0:1]
        if initial != prev_initial:
            distinct_initials = distinct_initials + initial
            prev_initial = initial
    print("Initials: " + distinct_initials)

    otl_utd_linkset_query = """
    PREFIX dct: <http://purl.org/dc/terms/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    SELECT ?otl_concept (GROUP_CONCAT(STR(?utd_concept); separator=";") AS ?utd_concepts) (GROUP_CONCAT(STR(?label); separator=";") AS ?utd_labels)
        WHERE {
            GRAPH <https://data.rws.nl/def/otl/graaf-otl-utd-linkset> {
                ?otl_concept dct:conformsTo ?utd_concept .
            }
            OPTIONAL {
                GRAPH <https://data.rws.nl/def/utd/graaf-kennismodel> {
                ?utd_concept skos:prefLabel ?label
                }
            }
        }
    GROUP BY ?otl_concept
    """

    otl_utd_linkset = []

    for row in ds.query(otl_utd_linkset_query):
        utd_raw = row["utd_concepts"]
        utd_concepts = [uri.strip() for uri in utd_raw.split(";")] if utd_raw else []

        utd_labels_raw = row["utd_labels"]
        utd_labels = [uri.strip() for uri in utd_labels_raw.split(";")] if utd_labels_raw else []

        otl_utd_linkset.append({
            "otl_concept": row["otl_concept"],
            "utd_concepts": utd_concepts,
            "utd_labels": utd_labels
        })


    print("... Attributes")
    patroon_query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX sh: <http://www.w3.org/ns/shacl#>
    SELECT ?resource ?resourcedef ?res ?datatype ?description ?name ?nodekind ?path ?minexclusive ?maxexclusive
    WHERE {
        GRAPH <https://data.rws.nl/def/otl/graaf-informatiemodel>  {
            ?res a sh:NodeShape .
            ?res sh:description ?resourcedef .
            ?res sh:property ?resource .
                ?resource a sh:PropertyShape .
            OPTIONAL { ?resource sh:datatype ?datatype .}
            OPTIONAL { ?resource sh:description ?description .}
            OPTIONAL { ?resource sh:name ?name .}
            OPTIONAL { ?resource sh:nodeKind ?nodekind .}
            OPTIONAL { ?resource sh:maxExclusive ?minexclusive .}
            OPTIONAL { ?resource sh:minExclusive ?maxexclusive .}
        } 
    }
    """

    patroon_results_array = []
    patroon_results = ds.query(patroon_query)

    for row in patroon_results:
        result_dict = {
            "resource": row["resource"].toPython(),
            "datatype": row["datatype"],
            "description": row["description"],
            "name": row["name"].toPython(),
            "nodekind": row["nodekind"].toPython(),
            "minexclusive": row["minexclusive"],
            "maxexclusive": row["maxexclusive"],
            "resourcedef": row["resourcedef"],
            "res": row["res"].toPython(),
        }
        patroon_results_array.append(result_dict)
    patroon_results_sorted = sorted(patroon_results_array, key=lambda x: (x["res"], x["resource"]))

    lineNo = 0
    for entry in patroon_results_sorted:
        lineNo += 1
    print("Aantal attributen:" + str(lineNo))

    initials = ""

    with open(
        f'{args["root"]}/kernregister-catalogus/md-doc/otl-list.md', "w"
    ) as md_otl_list:

        # Voorbereiding otl-list.md
        md_otl_list.write("---\ntitle: OTL-concepten (alfabetisch)\nparent: RWS Informatieconcepten\nnav_order: 1\n---\n")
        md_otl_list.write(
            "\n## Introductie\nDeze pagina bevat een alfabetisch overzicht van alle OTL-concepten.\n## Alfabetisch overzicht\n"
        )

        prev_initial = ""
        section = ""
        for entry in results_array:
            entry_str = entry["label"]
            initial = entry_str[0:1]
            initials = initials + initial
            if initial != prev_initial:
                skip_initial_comma = 1
                if section != "":
                    md_otl_list.write(f"### {prev_initial}\n")
                    md_otl_list.write(f"{section}\n")
                    section = wrap_h3(prev_initial) + section
                    section = wrap_section(section)
                    section = ""
            if skip_initial_comma == 1:
                skip_initial_comma = 0
            else:
                section = section + (", ")
            section = section + wrap_href(entry_str, initial)
            prev_initial = initial
        section = wrap_h3(prev_initial) + section
        section = wrap_section(section)

    # Laad mapping data
    with open(f"{args['root']}/mapping.json", "r", encoding="utf-8") as mapping_file:
        mapping_data = json.load(mapping_file)

    print("- Stage 2")

    for char in distinct_initials:
        print("Writing file: " + char)
        md_filename = f'{args["root"]}/kernregister-catalogus/md-doc/concepten-' + char + ".md"
        with open(md_filename, "w") as md_output:
            # Voorbereiding markdown file
            md_output.write(
                f"---\ntitle: OTL-concepten ({char})\nparent: OTL-concepten (alfabetisch)\nnav_order: 1\n---\n"
            )
            md_output.write(
                f"\n## Introductie\nDeze pagina bevat een overzicht van alle OTL-concepten beginnend met de letter '{char}'.\n## Overzicht\n"
            )

            for entry in results_array:
                entry_str = entry["label"]
                defi = entry["definition"]
                brdr = entry["broader"].toPython()
                initial = entry_str[0:1]
                section = ""
                md_section = ""

                if initial == char:
                    md_section += f"## {entry_str}\n\n"
                    md_section += f"{defi}  \n\n"
                    md_section += f"Breder begrip: [{brdr}]({brdr})  \n\n"
                    section = section + wrap_h2(entry_str)
                    section = section + wrap_p(defi)
                    section = section + "Breder begrip: " + brdr
                    if args["verbose"]:
                        print("Resource: " + get_last_word(entry["resource"].toPython()))
                    patroon_data = ""
                    row_data = ""
                    for pattern in patroon_results_sorted:
                        if get_last_word(pattern["res"]) == get_last_word(entry["resource"].toPython()):
                            patroon_data = ""
                            patroon_data = patroon_data + wrap_td(pattern["name"])
                            if args["verbose"]:
                                print("patroon: " + pattern["name"])
                            if not pattern["datatype"]:
                                datatype = ""
                            else:
                                datatype = remove_uri_prefix(pattern["datatype"])

                            nodekind = remove_uri_prefix(pattern["nodekind"])

                            patroon_data = patroon_data + wrap_td(unquote(quote(datatype)))
                            patroon_data = patroon_data + wrap_td(pattern["minexclusive"])
                            patroon_data = patroon_data + wrap_td(pattern["maxexclusive"])
                            patroon_data = patroon_data + wrap_td(unquote(quote(nodekind)))
                            patroon_data = patroon_data + wrap_td("")  # Keuzelijst

                            try:
                                bms_data = []
                                bms_props = mapping_data[str(entry_str)][pattern["name"]]
                                for bms in bms_props:
                                    name = bms_props[bms]['name-bms']
                                    if name == "ultimo":
                                        name = "ultimo"
                                    elif name == "disk":
                                        name = "Disk"
                                    elif name == "bkn":
                                        name = "BKN"
                                    elif name == "kerngis":
                                        name = "Kerngis"

                                    if bms_props[bms]["datatype-bms"] == bms_props[bms]["datatype-otl"]:
                                        bms_data.append(
                                            f"<b>{bms}</b>: {name} (<font color=\"green\">{bms_props[bms]['datatype-bms']}</font>)"
                                        )
                                    else:
                                        bms_data.append(
                                            f"<b>{bms}</b>: {name} (<font color=\"red\">{bms_props[bms]['datatype-bms']}</font>)"
                                        )
                                patroon_data = patroon_data + wrap_td("<br>".join(bms_data))
                            except:
                                patroon_data = patroon_data + wrap_td("")

                            patroon_data = wrap_tr(patroon_data)
                            row_data = row_data + patroon_data
                    header = wrap_th("Kenmerk")
                    header = header + wrap_th("Gegevenstype")
                    header = header + wrap_th("Max. waarde")
                    header = header + wrap_th("Min. waarde")
                    header = header + wrap_th("Waardetype")
                    header = header + wrap_th("Keuzelijst")
                    header = header + wrap_th("BMS")
                    header = wrap_tr(header)
                    table_data = header + row_data
                    table_data = wrap_table(table_data)
                    section = section + wrap_h3("Kenmerken")
                    section = section + table_data
                    if row_data != "":
                        md_section += f"### Kenmerken\n{table_data}\n"

                    # If the OTL concept is linked to one or more UTD concepts, add the UTD concepts to a table.
                    row_data = ""
                    for otl_utd_link in otl_utd_linkset:
                        if otl_utd_link["otl_concept"] == entry['resource']:
                            for i, utd_concept in enumerate(otl_utd_link["utd_concepts"]):
                                utd_row_data = wrap_td(utd_concept)
                                utd_row_data += wrap_td(otl_utd_link["utd_labels"][i])
                                row_data += wrap_tr(utd_row_data)

                    if row_data != "":
                        header = wrap_th("UTD concept")
                        header = header + wrap_th("Label")
                        header = wrap_tr(header)

                        utd_table = wrap_table(header + row_data)
                        md_section += f"### UTD concepten\n{utd_table}\n"

                    md_output.write(md_section)

    end_time = time.time()
    run_time = end_time - start_time
    print(f"Complete run in {run_time} seconds")
    print("\n")


def parse_args():
    parser = argparse.ArgumentParser(description="Genereer documentatie voor de kernregistratie.")
    parser.add_argument(
        "root",
        help="Pad naar de root directory van de kernregistratie-repository. Indien niet gegeven wordt de huidige directory ('.') gebruikt.",
        nargs="?",
        default=os.getcwd(),
    )
    parser.add_argument(
        "-v", "--verbose", help="Geef extra output ter ondersteuning van ontwikkelen of debuggen.", action="store_true"
    )
    args = parser.parse_args()

    return {
        "root": args.root,
        "verbose": args.verbose
    }


def get_all_keywords(current_kr, kr_dict):
    # current_kr is de URI van de KR waarvan we de keywords willen hebben
    ret = []
    seen = set()
    kw_seen = []
    for kr in kr_dict:
        kw = ""
        if kr["dataset"] == current_kr:
            kw = kr["keyword"]
            if kw not in seen:
                seen.add(kw)
                ret.append(kw)
    return ret


def get_all_dataservices(current_kr, kr_dict):
    ret = []
    seen = set()
    service_seen = []
    for kr in kr_dict:
        if kr["dataset"] == current_kr:
            service = kr["dataservice"]
            if service not in service_seen:
                seen.add(service)
                ret.append(service)
    return ret


def get_dataservice_name(service, kr_dict):
    for row in kr_dict:
        if row["dataservice"] == service:
            return row["servicename"]


def get_dataservice_url(service, kr_dict):
    for row in kr_dict:
        if row["dataservice"] == service:
            return row["endpdescr"]

def get_first_initial_last_word(input_str):
    last_word = get_last_word(input_str)
    return last_word[0].upper()


def get_last_word(input_str):
    last_word = input_str.strip("/").split("/")[-1]
    return last_word


def remove_uri_prefix(uri_str):
    # Split the URI on the last occurence of "/" and only keep the part after it
    return uri_str.rsplit("/", 1)[1]


def wrap_section(wrapstr):
    return_str = "<section>\n" + wrapstr + "\n</section>\n"
    return return_str


def wrap_h3(wrapstr):
    return_str = "\n<h3>" + wrapstr + "</h3>\n"
    return return_str


def wrap_h2(wrapstr):
    return_str = "\n<h2>" + wrapstr + "</h2>\n"
    return return_str


def wrap_anchor(wrapstr):
    return_str = '<a name="' + wrapstr + '"></a>\n'
    return return_str


def wrap_href(wrapstr, initial):
    return_str = (
        '<a href="concepten-' + initial + ".html#" + wrapstr.replace(" ", "-").lower() + '"> ' + wrapstr + "</a>\n"
    )
    return return_str


def wrap_href_simple(wrapstr, url):
    return_str = '<a href="' + url + '"> ' + wrapstr + "</a>\n"
    return return_str

def wrap_href_simple (wrapstr, url):
    return_str = "<a href=\"" + url + "\"> " + wrapstr + "</a>\n"
    return return_str

def wrap_p (wrap_str):
    return_str = "<p>" + wrap_str + "</p>"
    return return_str


def wrap_table(wrap_str):
    return_str = '<table style="vertical-align: top;">\n' + wrap_str + "</table>\n"
    return return_str


def wrap_tr(wrap_str):
    return_str = '<tr style="vertical-align:top">\n' + wrap_str + "</tr>\n"
    return return_str


def wrap_th(wrap_str):
    return_str = (
        '<th style="padding: 5px 20px;font-weight: bold; vertical-align: top; background-color: rgba(211,211,211,0.2);">'
        + wrap_str
        + "</th>\n"
    )
    return return_str


def wrap_td(wrap_str, span=1, align="left"):
    if not isinstance(wrap_str, str):
        wrap_str = ""
    return_str = (
        f'<td colspan="{span}" style="text-align: {align}; padding: 10px 20px; vertical-align: top; background-color: rgba(211,211,211,0.5);">\n'
        + wrap_str
        + "</td>\n"
    )
    return return_str


def wrap_tdfc(wrap_str, span=1, align="left"):
    if not isinstance(wrap_str, str):
        wrap_str = ""
    return_str = (
        f'<td colspan="{span}" style="text-align: {align}; padding: 10px 20px; vertical-align: top; background-color: rgba(211,211,211,0.2);">\n'
        + wrap_str
        + "</td>\n"
    )
    return return_str

def get_all_keywords (current_kr, kr_dict):
    # current_kr is de URI van de KR waarvan we de keywords willen hebben
    ret = []
    seen = set()
    kw_seen = []
    for kr in kr_dict:
        kw=""
        if  kr['dataset'] == current_kr:
            kw = kr['keyword']
            if kw not in seen:
                seen.add(kw)
                ret.append(kw)
    return ret           


def get_all_dataservices(current_kr, kr_dict):
    ret = []
    seen = set()
    service_seen = []
    for kr in kr_dict:
        if kr['dataset'] == current_kr:
            service = kr['dataservice']
            if service not in service_seen:
                seen.add(service)
                ret.append(service)
    return ret
  

def get_dataservice_name (service, kr_dict):
    for row in kr_dict:
        if row['dataservice'] == service:
            return row['servicename']


def get_dataservice_url(service, kr_dict):
    for row in kr_dict:
        if row['dataservice'] == service:
            return row['endpdescr']

if __name__ == "__main__":
    main()
