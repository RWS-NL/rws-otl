# Deployment
Momenteel wordt de OTL-viewer gedoployed naar Github pages zodra er wordt gepusht naar de repo. Hier moet aan toegevoegd worden dat hij elke ochtend automatisch wordt gedeployed, zodat in het geval van een hack de OTL-viewer niet permanent uit de lucht is.
## Aanpak
### Dagelijkse deployment
De dagelijkse deployment kan geautomatiseerd worden aan de hand van een cronjob. Dit kan gedaan worden door een schedule toe te voegen aan het on argument van de `build-and-demploy.yml` workflow:
```yaml
on:
    push:
        branches: ["main"]

    schedule:
    - cron: '0 6 * * *'
```
Deze cronjob zal elke dag om 6:00 de workflow triggeren.

# Mapping file
De mappingfile wordt bij elke deployment gegenereerd op basis van de csv bestanden op de airbim-mappingrule-generator repo. De CSV bestanden die gebruikt worden als bron zijn hier te vinden: https://github.com/RWS-NL/airbim-mappingrule-generator/tree/master/mappingregels 
Om het deployment script toegang te geven tot deze CSV bestanden is het nodig om een fine-grained token aan te maken. Dit moet gedaan worden op Github -> Settings -> Developer Settings -> Personal access tokens -> Fine-grained tokens. Hier moet een nieuwe token worden aangemaakt met de Repository permission "Read access to actions, code, and metadata" voor de RWS-NL organisatie. Vervolgens kan deze toegevoegd worden aan de repo van de OTL viewer onder Settings (van de repo) -> Secrets and variables -> actions -> Repository secrets. De naam van de secret moet "RWS_TOKEN" zijn en de eerder gegenereerde Fine-grained token is de value van de secret.

# Gebruikte Technologieën 
De OTL viewer maakt gebruik van een aantal technologieën. De licenties van deze technologieën zijn hieronder inzichtelijk gemaakt.

| Technologie | Licentie | Activiteit |
|-------------|----------|------------|
| RDFLib | [BSD 3-Clause](https://github.com/RDFLib/rdflib/blob/main/LICENSE) | Actief onderhouden, redelijk actieve Github issues |
| Jekyll | [MIT](https://github.com/jekyll/jekyll/blob/master/LICENSE) | Actief onderhouden, grote community |
| jekyll-toc | [MIT](https://github.com/jekyll/jekyll/blob/master/LICENSE) | Laatste update 10 maanden geleden, maar het is een lichtgewicht plugin voor genereren van table of content|
| Just the Docs | [MIT](https://github.com/just-the-docs/just-the-docs/blob/main/LICENSE.txt) | Actief onderhouden en activiteit in Github issues |
