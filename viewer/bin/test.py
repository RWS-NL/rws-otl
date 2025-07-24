from rdflib import Graph, ConjunctiveGraph, URIRef, Literal, Dataset

# Create a dataset and add separate graphs to it
dataset = Dataset()
graph1 = Graph()
graph2 = Graph()

# Add triples to graph1
graph1.add((URIRef('http://example.org/subject1'), URIRef('http://example.org/predicate1'), Literal('Object1')))

# Add triples to graph2
graph2.add((URIRef('http://example.org/subject2'), URIRef('http://example.org/predicate2'), Literal('Object2')))

# Add graphs to the dataset
dataset.add_graph(graph1)
dataset.add_graph(graph2)

# Perform a SPARQL query on the default graph
query_result = dataset.query('SELECT ?s ?p ?o WHERE { ?s ?p ?o }')

for row in query_result:
    print(row)
