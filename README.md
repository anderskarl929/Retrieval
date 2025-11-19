# Retrieval Övningsapplikation

En interaktiv webbapplikation för elever att öva retrieval med 1X2-frågor (flervalsfrågorfrågor med 3 alternativ). Resultat sparas automatiskt i Google Sheets för lärarens översikt.

## Funktioner

### För Elever
- ✅ Enkel inloggning med namn
- ✅ Interaktiva flervalsfrågorfrågor med 3 alternativ
- ✅ Omedelbar feedback på svaren
- ✅ Visuell progressbar
- ✅ Detaljerad resultatsammanfattning
- ✅ Betygsättning (A-F)
- ✅ Tidsstatistik

### För Lärare
- ✅ Elevinloggning - spåra vem som gör vilket test
- ✅ Automatisk sparning av resultat till Google Sheets
- ✅ Se alla elevresultat på ett ställe
- ✅ Detaljerad fråga-för-fråga genomgång för varje elev
- ✅ Färgkodade resultat baserat på betyg
- ✅ Exportera data för vidare analys
- ✅ Ladda upp egna frågefiler (CSV-format)
- ✅ **AI Frågegenerator - Generera frågor automatiskt från text!**

## 🤖 AI Frågegenerator - NYT!

**Spara tid med AI!** Generera automatiskt 1X2-frågor från vilken text som helst.

### Snabbstart Frågegenerator

1. **Öppna `fragegenerator.html` i webbläsaren**
2. **Skaffa API-nyckel:**
   - Gå till [Anthropic Console](https://console.anthropic.com/) eller [OpenAI Platform](https://platform.openai.com/)
   - Skapa gratis konto (får $5 i gratis krediter)
   - Skapa API-nyckel
3. **Klistra in text** du vill skapa frågor från
4. **Klicka "Generera Frågor"**
5. **Ladda ner CSV** och använd direkt i quiz-appen!

**Läs mer:** Se `FRAGEGENERATOR_README.md` för fullständig guide

**Filer:**
- `fragegenerator.html` - Web-baserad generator (enklast!)
- `fragegenerator.py` - Python-version för avancerade användare
- `exempel_text_historia.txt` - Exempeltext att testa med

**Kostnad:** ~1 kr per 100 genererade frågor

## Snabbstart

### För Lärare - Första gången

1. **Öppna lärar-dashboarden**
   - Öppna `larar-dashboard.html` i en webbläsare
   - Följ steg-för-steg instruktionerna för att sätta upp Google Sheets

2. **Konfigurera Google Sheets** (engångsinställning)
   - Se detaljerade instruktioner i `larar-dashboard.html`
   - Eller följ "Google Sheets Setup" nedan

3. **Dela med elever**
   - Dela filen `1x2_fragor.html` med dina elever
   - Klistra in Google Sheets Web App URL i applikationen

### För Elever

1. **Öppna applikationen**
   - Öppna `1x2_fragor.html` i en webbläsare

2. **Logga in**
   - Ange ditt för- och efternamn
   - Klicka "Starta Quiz"

3. **Ladda upp frågefil**
   - Välj CSV-fil med frågor (läraren ger dig denna)
   - Eller använd `exempel_fragor.csv` för att testa

4. **Gör testet**
   - Svara på frågorna
   - Få direkt feedback

5. **Se dina resultat**
   - Resultat sparas automatiskt till läraren
   - Du kan också ladda ner dina egna resultat

## Google Sheets Setup (För Lärare)

### Detaljerade Instruktioner

**Steg 1: Skapa Google Sheets**
1. Gå till [Google Sheets](https://sheets.google.com)
2. Skapa ett nytt kalkylblad
3. Döp det till t.ex. "Elevresultat Historia 2024"

**Steg 2: Öppna Apps Script**
1. Klicka på `Extensions` → `Apps Script`
2. En ny flik öppnas

**Steg 3: Klistra in Script**
1. Ta bort all befintlig kod
2. Öppna filen `google-apps-script.js`
3. Kopiera hela innehållet och klistra in
4. Klicka på "Spara" (💾)

**Steg 4: Deploya Web App**
1. Klicka på `Deploy` → `New deployment`
2. Välj typ: `Web app`
3. Sätt inställningar:
   - **Execute as:** Me
   - **Who has access:** Anyone
4. Klicka `Deploy`
5. Godkänn behörigheter om du tillfrågas

**Steg 5: Kopiera URL**
1. Kopiera "Web App URL" (ser ut som: `https://script.google.com/macros/s/.../exec`)
2. Klistra in denna URL i quiz-applikationen under "Lärarinställningar"

### Vad sparas i Google Sheets?

Två blad skapas automatiskt:

**1. Resultatsammanfattning**
- Tidpunkt
- Elevens namn
- Antal frågor, rätt/fel svar
- Procent och betyg
- Tid som spenderats

**2. Detaljerade Svar**
- Varje fråga eleven fick
- Elevens svar
- Rätt svar
- Om det var rätt eller fel

## Hur man använder (Detaljerat)

### Steg 1: Inloggning
- Eleven anger sitt för- och efternamn
- Läraren klistrar in Google Sheets Web App URL (behövs bara första gången)

### Steg 2: Ladda upp CSV-fil
- Klicka på "Välj CSV-fil"
- Välj frågefil (se CSV-format nedan)

### Steg 3: Svara på frågor
- Klicka på rätt alternativ
- Få omedelbar feedback
- Klicka "Nästa fråga"

### Steg 4: Se resultat
- Omfattande sammanfattning visas
- Resultat sparas automatiskt till Google Sheets
- Ladda ner egna resultat (valfritt)

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
