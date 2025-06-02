# de mapping bestanden uiteengeplozen
Zie hier: https://github.com/RWS-NL/airbim-mappingrule-generator/tree/master/resources/Input, maar kijk in de map mappingregels.

disk;
> https://data.rws.nl/def/disk/tbl_beheerobject;
> https://data.rws.nl/def/otl/Viaduct; 
> <https://data.rws.nl/def/disk/tbl_beheerobject-beheerobjectsoortid>;
;					;
> https://data.rws.nl/id/disk/tbl_beheerobjectsoort-196;
> http://purl.org/dc/terms/subject;
> https://data.rws.nl/def/otl/Viaduct;;;;;;

disk;
  https://data.rws.nl/def/disk/tbl_beheerobject;
  https://data.rws.nl/def/otl/Viaduct;
  <https://data.rws.nl/def/disk/tbl_beheerobject-naam>;
;
;
https://data.rws.nl/def/otl/naam;
;
http://www.opengis.net/ont/geosparql#hasGeometry;
http://www.w3.org/1999/02/22-rdf-syntax-ns#type;
http://www.opengis.net/ont/gml#Point;
http://www.w3.org/2001/XMLSchema#string;http://www.w3.org/2001/XMLSchema#string;

disk;
  https://data.rws.nl/def/disk/tbl_beheerobject;
  https://data.rws.nl/def/otl/Viaduct;
  <https://data.rws.nl/def/disk/tbl_beheerobject-stichtingsjaar>;
;
;
  https://data.rws.nl/def/otl/bouwjaar;
;
http://www.opengis.net/ont/geosparql#hasGeometry;
http://www.w3.org/1999/02/22-rdf-syntax-ns#type;
http://www.opengis.net/ont/gml#Point;
http://www.w3.org/2001/XMLSchema#long;
http://www.w3.org/2001/XMLSchema#gYear;


;-----
ultimo;
https://data.rws.nl/def/ultimo/processfunction;
https://data.rws.nl/def/otl/Viaduct;
<https://data.rws.nl/def/ultimo/processfunction-prfeqmtid>;
;					
https://data.rws.nl/id/ultimo/eqmtype-01209;
http://purl.org/dc/terms/subject;
https://data.rws.nl/def/otl/Viaduct;;;;;;

ultimo;
https://data.rws.nl/def/ultimo/processfunction;
https://data.rws.nl/def/otl/Viaduct;
<https://data.rws.nl/def/ultimo/processfunction-prfmanufyear>;
;
;
https://data.rws.nl/def/otl/bouwjaar;
;
http://www.opengis.net/ont/geosparql#hasGeometry;
http://www.w3.org/1999/02/22-rdf-syntax-ns#type;
http://www.opengis.net/ont/gml#Point;
http://www.w3.org/2001/XMLSchema#long;
http://www.w3.org/2001/XMLSchema#gYear;

ultimo;
https://data.rws.nl/def/ultimo/processfunction;
https://data.rws.nl/def/otl/Viaduct;
<https://data.rws.nl/def/ultimo/processfunction-_prfvorm>/<https://data.rws.nl/def/ultimo/_constructievormrcb-_cvrcbdescr>;
;
;
https://data.rws.nl/def/otl/constructievorm;
;
http://www.opengis.net/ont/geosparql#hasGeometry;
http://www.w3.org/1999/02/22-rdf-syntax-ns#type;
http://www.opengis.net/ont/gml#Point;
http://www.w3.org/2001/XMLSchema#string;
http://www.w3.org/2001/XMLSchema#string;



# hoe we hier gebruik van maken



Het patroon waar we volgens mij op moeten aansluiten:

Als de entry een http://purl.org/dc/terms/subject bevat is het een algemeen element dat een begrip introduceert (en dus de aansluiting bij
de otl vorm). Dat is de 6e positie van de entry.
Als die positie niet een http://purl.org/dc/terms/subject is, is het een kenmerk. 
Dat kenmerk verwijst naar:

    otl-patroon:bouwjaar a sh:PropertyShape ;
        sh:datatype xsd:gYear ;
        sh:description "bouwjaar-patroon"@nl ;
        sh:maxExclusive "2100"^^xsd:gYear ;
        sh:minExclusive "1594"^^xsd:gYear ;
        sh:name "bouwjaar"@nl ;
        sh:nodeKind sh:Literal ;
>        sh:path otl:bouwjaar .

en bijvoorbeeld 


In de informatiegraaf
    otl-patroon:naam a sh:PropertyShape ;
        sh:datatype xsd:string ;
        sh:description "naam-patroon"@nl ;
        sh:name "naam"@nl ;
        sh:nodeKind sh:Literal ;
>        sh:path otl:naam .

Als je kijkt naar otl:constructievorm (laatste voorbeeld uit de mappingen):

Dit staat in de informatiegraaf:

    otl-patroon:Aandrijving a sh:NodeShape ;
        sh:closed true ;
        sh:description "Basispatroon voor het vastleggen van Aandrijving"@nl ;
        sh:ignoredProperties ( dct:subject dct:coverage rdf:type bs:hasPart otl:isBeschrevenDoor geo:hasGeometry ) ;
        sh:name "Aandrijving"@nl ;
        sh:property otl-patroon:QRcode,
            otl-patroon:RWSconcept-Aandrijving,
            otl-patroon:barcode,
            otl-patroon:bouwdatum,
>            otl-patroon:constructievorm-Aandrijving,
            otl-patroon:datumInbedrijfname,
            otl-patroon:datumUitbedrijfname,
            otl-patroon:discipline-Onderdeel,
            otl-patroon:functioneleEigenschap-Aandrijving,
            otl-patroon:garantietermijn,
            otl-patroon:isFaalkanskritisch,
            otl-patroon:isWisseldeel,
            otl-patroon:materiaal,
            otl-patroon:materiaal1-Aandrijving,
            otl-patroon:materiaal2-Aandrijving,
            otl-patroon:merk,
            otl-patroon:omschrijving,
            otl-patroon:theoretischeLevensduur,
            otl-patroon:type,
            otl-patroon:vervultFaunavoorzieningsfunctie ;
        sh:target [ a sh:SPARQLTarget ;
                sh:select """SELECT ?this WHERE {
                    ?this <http://purl.org/dc/terms/subject> <https://data.rws.nl/def/otl/Aandrijving>
                }""" ] .

Er zijn heel veel objecttypes die een constructievorm gebruiken. Bijvoorbeeld:

    otl-patroon:constructievorm-Wegmarkering a sh:PropertyShape ;
        sh:datatype xsd:string ;
        sh:description "constructievorm-Wegmarkering-patroon"@nl ;
        sh:in ( "wegdekreflector" ) ;
        sh:name "constructievorm"@nl ;
        sh:nodeKind sh:Literal ;
>        sh:path otl:constructievorm .

Maar al die entries verwijzen naar die ene entry aan het eind.
Volgens mij moeten we dus daarvandan steeds 'omhoog' werken.
We weten dat we een OTL:constructievorm genereren in de mapping en dus in de data.
Als we daar bijhouden voor welk object type we dat doen kunnen we volgens mij die mapping per type/kenmerk uitlijsten.
Of ben ik hier wat te optimistisch? Misschien gewoon proberen en kijken waar we uitkomen? Gaat mogelijk sneller dan een diepgaande analyse.


