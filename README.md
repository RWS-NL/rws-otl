![Logo Rijkswaterstaat - Ministerie van Infrastructuur en Waterstaat](https://github.com/RWS-NL/rws-otl/assets/467305/13932dd5-c2c1-4fb0-9cca-d93ba02b5076)

# Rijkswaterstaat OTL

Welkom op de officiele, openbare Git repository van de Rijkswaterstaat Object Type Library (OTL). In deze repository vind je de technische files van de meest recente versie van de Rijkswaterstaat OTL. 

De OTL is een actueel en praktisch toepasbaar informatiemodel dat is opgebouwd door open W3C Linked Data standaarden te volgen en te implementeren. De OTL beschrijft de verschillende typen (informatie)objecten die voorkomen in het Rijkswaterstaat areaal met een eenduidige beschrijving, maar definieert ook de relaties tussen deze objecten, de kenmerken die ze kunnen hebben en restricties die op deze kenmerken voor  kunnen komen.

> [!TIP]
> Als je meer wil weten, kijk dan vooral op de officiele [OTL Publicatieomgeving](https://otl.rws.nl/) voor algemene info over deze OTL, of bekijk de inhoud van OTL door naar de [RWS OTL Viewer](https://rijkswaterstaat.beta.otl-viewer.com/) te gaan. 

## Inhoud

- **[./ontology/def](./ontology/def):** Deze map bevat diverse '.Trig'-bestanden welke in samenhang de volledige RWS OTL vormen. Ook staan er in de map [kaders](./ontology/def/kaders) enkele andere modellen beschreven, welke aan de OTL gekoppeld worden door middel van de linkset-bestanden in de [linkset](./ontology/def/linksets) map. [Trig](https://www.w3.org/TR/trig/) bestanden lijken op [Turtle](https://www.w3.org/TR/turtle/) bestanden, maar bieden de mogelijkheid om het model expliciet op te delen in grafen, wat in het geval van deze OTL zorgt voor een modulaire structuur waar per 'informatieproduct' naar de bijbehorende informatiebehoefte gekeken kan worden.
  
	**- [otl](./ontology/def/otl):**
 		-[informatieproducten](./ontology/def/otl/informatieproduct):
   
 	**- [kaders](./ontology/def/kaders):**
    
	**- [linksets](./ontology/def/linksets):**
