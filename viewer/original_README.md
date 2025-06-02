![Logo Rijkswaterstaat - Ministerie van Infrastructuur en Waterstaat](https://github.com/RWS-NL/rws-otl/assets/467305/13932dd5-c2c1-4fb0-9cca-d93ba02b5076)

# Rijkswaterstaat OTL

Welkom op de officiele, openbare Git repository van de Rijkswaterstaat Object Type Library (OTL). In deze repository vind je de technische files van de meest recente versie van de Rijkswaterstaat OTL. 

De OTL is een actueel en praktisch toepasbaar informatiemodel dat is opgebouwd door open W3C Linked Data standaarden te volgen en te implementeren. De OTL beschrijft de verschillende typen (informatie)objecten die voorkomen in het Rijkswaterstaat areaal met een eenduidige beschrijving, maar definieert ook de relaties tussen deze objecten, de kenmerken die ze kunnen hebben en restricties die op deze kenmerken voor  kunnen komen.

> [!TIP]
> Als je meer wil weten, kijk dan vooral op de officiele [OTL Publicatieomgeving](https://otl.rws.nl/) voor algemene info over deze OTL, of bekijk de inhoud van OTL door naar de [RWS OTL Viewer](https://rijkswaterstaat.beta.otl-viewer.com/) te gaan. 

## Inhoud

- **[./ontology/def](./ontology/def):** Deze map bevat diverse '.Trig'-bestanden welke in samenhang de volledige RWS OTL vormen. Ook staan er in de map [kaders](./ontology/def/kaders) enkele andere modellen beschreven, welke aan de OTL gekoppeld worden door middel van de linkset-bestanden in de [linkset](./ontology/def/linksets) map. [Trig](https://www.w3.org/TR/trig/) bestanden lijken op [Turtle](https://www.w3.org/TR/turtle/) bestanden, maar bieden de mogelijkheid om het model expliciet op te delen in grafen, wat in het geval van deze OTL zorgt voor een modulaire structuur waar per 'informatieproduct' naar de bijbehorende informatiebehoefte gekeken kan worden.
  
	**- [otl](./ontology/def/otl):** Dit is waar de complete RWS OTL te vinden is. Onderstaande afbeelding geeft de gelaagdheid van het model weer, waarbij:
    - het 'kennismodel' de klassen en kenmerken definieert en de taxonomische structuur die deze ten opzichte van elkaar hebben. 
    - het 'informatiemodel' waar restricties vastgelegd worden zoals _het kenmerk bouwjaar moet wanneer ingevuld tussen de waardes 1594 en 2100 liggen_ .
    - de '[informatieproducten](./ontology/def/otl/informatieproduct)' waar restricties vastgelegd worden die specifiek gelden voor een bepaald proces zoals _voor het proces 'prestatiegestuurd instandhoudingsplan' móet het kenmerk bouwjaar ingevuld zijn bij het object viaduct_ . Dit kan aan de hand van deze restricties gecontroleerd worden in beheersystemen zoals Ultimo.
  
		![Opbouw gelaagdbeid Rijkswaterstaat OTL](https://github.com/RWS-NL/rws-otl/assets/109587932/c1afc4c5-d018-4b4d-91fc-733fd0b3f461)
   
 	**- [kaders](./ontology/def/kaders):** Kaders zijn externe modellen die los staan van de OTL zelf. Deze externe modellen kunnen handig zijn om met een bepaalde 'view' naar de RWS OTL te kijken, bijvoorbeeld die van de NEN2767-4. Opgenomen kaders zijn op dit moment:
    - NEN2767
    - SATO
    - Uniforme Technische Decompositie (UTD)
    
	**- [linksets](./ontology/def/linksets):** Linksets beschrijven de mapping tussen klassen in een extern model en klassen in de OTL. Zo kan de OTL bekeken worden met een specifiekere view, zoals de NEN2767 of de Algemene Begrippen en Definitielijst van Rijkswaterstaat.  

    **- [kernregistraties]( ./ontology/kernregister-catalogus ):** Kernregistraties beschrijven de datasets die Rijkswaterstaat beschouwt als centrale datasets.  De kernregistratie worden beschreven inclusief de ontsluitingsmechanismes. In de [kernregistratiebeschrijving](./kernregister-catalogus/kr-beschrijving.html) wordt op toegangkelijke manier toegang gegeven tot de kernregistraties en de er mee samennhangende modellen zoals de OTL en het RWS bedrijfsobjecten model. 
