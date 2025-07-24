from rdflib import Dataset, URIRef

def search_row(data_table, search_key):
    for row in data_table:
        if row.get('resource').toPython() == search_key.toPython():
            return row
    return None

# Create an empty ConjunctiveGraph
ds = Dataset()

# Parse multiple .trig files into the graph
files = [ \
          '/home/gja/Development/rws-kernregistratie/rws-otl/ontology/def/otl/graaf-kennismodel.trig', \
          '/home/gja/Development/rws-kernregistratie/rws-otl/ontology/def/otl/graaf-informatiemodel.trig', \
#         '/home/gja/Development/rws-kernregistratie/rws-otl/ontology/def/otl/graaf-kennismodel-bomr.trig', \
#         '/home/gja/Development/rws-kernregistratie/rws-otl/ontology/def/otl/graaf-informatiemodel.trig', \
         ]
for file in files:
    ds.parse(file, format='trig')

query = """
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
        } }
"""

patroon_results_array = []

patroon_results = ds.query(query)

for row in patroon_results:
    result_dict = {'resource': row['resource'].toPython(), 'datatype': row['datatype'], 'description': row['description'], 'name': row['name'], 'nodekind': row['nodekind'].toPython(), 'minexclusive': row['minexclusive'], 'maxexclusive': row['maxexclusive'], 'resourcedef': row['resourcedef'], 'res': row['res'].toPython()}
    patroon_results_array.append(result_dict)
patroon_results_sorted = sorted (patroon_results_array, key=lambda x: (x['res'], x['resource']))

    
line_no = 0
for patroon in patroon_results_sorted:
    line_no = line_no + 1
    if line_no > 20:
        break
    print ((patroon['resource']) + ": " + patroon ['res'] + "/: " + patroon['name'] + " = " + patroon['description'] + " .. " + patroon['nodekind'] + "-=-"  + patroon ['datatype'].toPython()  )
    print ("\n")

# print ('existence test')
# search_key = URIRef('https://data.rws.nl/def/otl-patroon/PFcurve')

# result = search_row(patroon_results_array, search_key)
# if result:
#     print(result)
# else:
#     print("Row not found")

