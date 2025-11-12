# Retrieval Övningsapplikation

En interaktiv webbapplikation för elever att öva retrieval med 1X2-frågor (flervalsfrågorfrågor med 3 alternativ).

## Funktioner

### För Elever
- ✅ Interaktiva flervalsfrågorfrågor med 3 alternativ
- ✅ Omedelbar feedback på svaren
- ✅ Visuell progressbar
- ✅ Detaljerad resultatsammanfattning
- ✅ Betygsättning (A-F)
- ✅ Tidsstatistik

### För Lärare
- ✅ Ladda upp egna frågefiler (CSV-format)
- ✅ Få omfattande resultatsammanfattning
- ✅ Ladda ner resultat som CSV-fil
- ✅ Se detaljerad fråga-för-fråga genomgång

## Hur man använder

### Steg 1: Öppna applikationen
Öppna filen `1x2_fragor.html` i en webbläsare.

### Steg 2: Ladda upp en CSV-fil
Klicka på "Välj CSV-fil" och välj din frågefil. En exempelfil finns i `exempel_fragor.csv`.

### Steg 3: Svara på frågorna
Eleverna klickar på det alternativ de tror är rätt. Direkt feedback ges efter varje svar.

### Steg 4: Se resultaten
Efter sista frågan visas en omfattande resultatsammanfattning med:
- Total poäng och procent
- Antal rätt och fel svar
- Total tid
- Betyg (A-F)
- Detaljerad genomgång av alla frågor

### Steg 5: Ladda ner resultat (valfritt)
Klicka på "Ladda ner Resultat" för att spara resultaten som en CSV-fil.

## CSV-format

Frågefilen ska vara i följande format:

```
Fråga,Alternativ 1,Alternativ 2,Alternativ 3,Rätt svar (1/2/3)
```

### Exempel:
```
Vilket år startade första världskriget?,1912,1914,1916,2
Vem var Sveriges kung under andra världskriget?,Gustaf V,Gustaf VI Adolf,Carl XVI Gustaf,1
```

### Viktiga punkter:
- Separera fält med komma (`,`)
- Det rätta svaret anges med siffran 1, 2 eller 3
- Ingen rubrikrad behövs
- Använd `exempel_fragor.csv` som referens

## Betygsättning

Betyg baseras på procentandel rätt svar:
- **A**: 90-100%
- **B**: 80-89%
- **C**: 70-79%
- **D**: 60-69%
- **E**: 50-59%
- **F**: 0-49%

## Nedladdad resultatfil

Den nedladdade CSV-filen innehåller:
1. Resultatsammanfattning (datum, tid, antal frågor, resultat, betyg)
2. Detaljerad lista över alla frågor med elevens svar och rätt svar

## Support

För frågor eller problem, kontakta systemadministratören.
