# 🤖 AI Frågegenerator - Användardokumentation

Automatiskt generera 1X2-frågor från text med hjälp av AI!

## Översikt

Frågegeneratorn är en AI-agent som automatiskt skapar övningsfrågor från text du anger. Detta sparar dig massvis med tid när du ska skapa quiz för dina elever.

**Vad den gör:**
- Läser text du anger (t.ex. från lärobok, artikel, eller egna anteckningar)
- Analyserar innehållet och identifierar viktiga fakta
- Skapar frågor med tre svarsalternativ (ett rätt, två felaktiga)
- Genererar trovärdiga distraktorer (felaktiga alternativ)
- Exporterar färdiga frågor i CSV-format för quiz-appen

## Två versioner tillgängliga

### 1. Web-version (Rekommenderas för de flesta)

**Filer:** `fragegenerator.html`

**Fördelar:**
- Enkel att använda - öppna bara i webbläsaren
- Ingen installation behövs
- Visuell förhandsvisning av frågorna
- Fungerar på alla enheter

### 2. Python-version (För avancerade användare)

**Filer:** `fragegenerator.py`

**Fördelar:**
- Kan automatiseras via script
- Kan köras från kommandoraden
- Lättare att bearbeta stora mängder text
- Bättre för batch-generering

---

## 🌐 Web-version - Snabbguide

### Steg 1: Skaffa API-nyckel

Du behöver en API-nyckel från antingen:

**Alternativ A: Anthropic Claude (Rekommenderas)**
1. Gå till https://console.anthropic.com/
2. Skapa ett konto (eller logga in)
3. Gå till "API Keys"
4. Skapa en ny nyckel
5. Kopiera nyckeln (börjar med `sk-ant-...`)

**Alternativ B: OpenAI GPT**
1. Gå till https://platform.openai.com/
2. Skapa ett konto (eller logga in)
3. Gå till "API Keys"
4. Skapa en ny nyckel
5. Kopiera nyckeln (börjar med `sk-...`)

**Kostnad:** Båda tjänsterna erbjuder gratis krediter för nya användare. Därefter kostar det några kronor per 100 frågor.

### Steg 2: Öppna Frågegeneratorn

1. Öppna `fragegenerator.html` i din webbläsare
2. Välj AI-motor (Anthropic eller OpenAI)
3. Klistra in din API-nyckel

### Steg 3: Generera Frågor

1. **Välj ämne** - Välj från listan eller använd standard
2. **Ange antal frågor** - Rekommenderat: 5-10 per textavsnitt
3. **Klistra in text** - Texten du vill skapa frågor från
4. Klicka på **"Generera Frågor"**

### Steg 4: Ladda ner eller Kopiera

När frågorna är genererade kan du:
- **Ladda ner CSV** - Sparar direkt som CSV-fil
- **Kopiera CSV** - Kopierar till urklipp för att klistra in någon annanstans
- **Skapa fler frågor** - Börja om med ny text

### Exempel

**Input:**
```
Sverige blev medlem i EU 1995 efter en folkomröstning där 52,3% röstade ja.
Tillsammans med Sverige gick även Finland och Österrike med samma dag.
```

**Output:**
```csv
"Vilket år blev Sverige medlem i EU?","1993","1995","1997",2
"Hur många procent röstade ja i folkomröstningen om EU?","52,3%","48,7%","55,1%",1
"Vilka länder blev medlemmar i EU samtidigt som Sverige?","Finland och Danmark","Norge och Finland","Finland och Österrike",3
```

---

## 💻 Python-version - Guide

### Installation

```bash
# Installera nödvändiga paket
pip install anthropic  # För Anthropic Claude
# eller
pip install openai     # För OpenAI GPT
```

### Grundläggande användning

```bash
# Generera från textfil
python fragegenerator.py --input exempel_text_historia.txt --output fragor.csv --num 10

# Generera från text direkt
python fragegenerator.py --text "Sverige blev medlem i EU 1995" --num 3

# Använd specifikt ämne
python fragegenerator.py --input text.txt --subject "Historia" --num 5

# Använd OpenAI istället för Anthropic
python fragegenerator.py --input text.txt --api openai --num 5
```

### Miljövariabler

Istället för att ange API-nyckel varje gång kan du sätta en miljövariabel:

**Linux/Mac:**
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
# eller
export OPENAI_API_KEY="sk-..."
```

**Windows:**
```cmd
set ANTHROPIC_API_KEY=sk-ant-...
# eller
set OPENAI_API_KEY=sk-...
```

### Avancerade exempel

```bash
# Generera många frågor från stor textfil
python fragegenerator.py \
  --input kapitel_3_industriella_revolutionen.txt \
  --output fragor_kapitel_3.csv \
  --num 20 \
  --subject "Historia"

# Batch-generering från flera filer
for file in kapitel_*.txt; do
  python fragegenerator.py \
    --input "$file" \
    --output "fragor_${file%.txt}.csv" \
    --num 10
done
```

---

## 📝 Tips för Bästa Resultat

### Textval

**Bra text:**
- Tydliga fakta och information
- 100-500 ord per generering
- Välstrukturerad och läsbar
- Fokuserad på ett specifikt ämne

**Undvik:**
- För kort text (< 50 ord)
- För lång text (> 1000 ord) - dela upp i mindre delar istället
- Text med för många begrepp samtidigt
- Oklar eller tvetydig information

### Antal frågor

- **5-10 frågor** per textavsnitt ger bäst kvalitet
- För korta texter: max 3-5 frågor
- För längre texter: dela upp i avsnitt och generera 5-10 frågor per avsnitt

### Granskning

**Viktigt:** Granska alltid de genererade frågorna!
- Kontrollera att frågorna är korrekta
- Se till att distraktorer är trovärdiga men felaktiga
- Justera svårighetsgrad om nödvändigt
- Ta bort eller ändra frågor som inte passar

---

## 🎯 Användningsfall

### 1. Snabb quiz-skapande

**Scenario:** Du ska skapa ett quiz för imorgon
```
1. Ta text från läroboken (kopiera 1-2 sidor)
2. Klistra in i frågegeneratorn
3. Generera 10 frågor
4. Granska och justera om nödvändigt
5. Ladda ner CSV
6. Använd direkt i quiz-appen
```

### 2. Frågebank

**Scenario:** Bygg upp en stor frågebank
```
1. Generera 5-10 frågor per textavsnitt/kapitel
2. Spara varje fil med beskrivande namn (t.ex. "historia_ww2_kapitel1.csv")
3. Samla alla frågor i en mapp
4. Använd olika frågor för olika klasser/tillfällen
```

### 3. Repetition

**Scenario:** Skapa repetitionsfrågor från elevernas egna anteckningar
```
1. Låt eleven skriva en sammanfattning av kapitlet
2. Använd sammanfattningen för att generera frågor
3. Eleven får quiz baserat på sin egen text
4. Perfekt för att kontrollera förståelse
```

---

## ⚙️ Felsökning

### "API-anrop misslyckades"

**Lösning:**
- Kontrollera att API-nyckeln är korrekt
- Se till att du har krediter kvar på ditt konto
- Kontrollera internetanslutningen

### "Inga frågor genererades"

**Lösning:**
- Texten kan vara för kort - prova med mer text
- Texten kan vara för oklar - använd tydligare text
- Försök minska antal frågor

### "Frågorna är av dålig kvalitet"

**Lösning:**
- Använd mer välskriven och strukturerad text
- Minska antal frågor per generering
- Prova att dela upp texten i mindre avsnitt
- Specificera ämnet mer noggrant

### Python-version: "ModuleNotFoundError"

**Lösning:**
```bash
pip install anthropic
# eller
pip install openai
```

---

## 💰 Kostnad

### Anthropic Claude
- **Gratis krediter:** $5 för nya användare
- **Kostnad:** ~$0.01 per 10 frågor
- **100 frågor:** ~$0.10 (ca 1 kr)

### OpenAI GPT-4
- **Gratis krediter:** $5 för nya användare
- **Kostnad:** ~$0.02 per 10 frågor
- **100 frågor:** ~$0.20 (ca 2 kr)

**Konklusion:** Mycket billigt! Du kan generera hundratals frågor för några kronor.

---

## 🔒 Säkerhet & Integritet

- **API-nycklar:** Spara aldrig din API-nyckel i filer eller dela den med andra
- **Data:** Din text skickas till AI-tjänsten för bearbetning
- **GDPR:** Undvik att skicka personuppgifter om elever
- **Rekommendation:** Använd endast läromaterialtext, inga elevdata

---

## 📚 Exempel på Användning

### Exempel 1: Historia

**Input (exempel_text_historia.txt):**
```
Den industriella revolutionen började i England under mitten av 1700-talet.
James Watts ångmaskin från 1769 revolutionerade produktionen.
Den första järnvägen öppnades 1825 mellan Stockton och Darlington.
```

**Kommando:**
```bash
python fragegenerator.py --input exempel_text_historia.txt --num 5
```

**Resultat:**
5 frågor om den industriella revolutionen sparade i `genererade_fragor.csv`

### Exempel 2: Direkt text

**Kommando:**
```bash
python fragegenerator.py \
  --text "Fotosyntesen är processen där växter omvandlar solljus till energi" \
  --subject "Biologi" \
  --num 3 \
  --output biologi_fotosyntes.csv
```

---

## 🎓 Pedagogiska Tips

### Variera svårighetsgrad

- Be AI:n skapa "enkla" eller "svåra" frågor genom att lägga till det i texten
- Kombinera frågor från olika texter för varierad svårighetsgrad

### Använd för formativ bedömning

- Skapa korta quiz efter varje lektion
- Använd resultat för att identifiera vad elever behöver repetera
- Anpassa undervisningen baserat på resultat

### Engagera elever

- Låt elever skapa sina egna sammanfattningar
- Generera frågor från elevernas texter
- Elever quiz varandra med AI-genererade frågor

---

## 🆘 Support

Om du stöter på problem:

1. **Läs felsökningssektionen** ovan
2. **Kontrollera att du har senaste versionen** av filerna
3. **Testa med exempeltexten** först
4. **Kontakta teknisk support** om problemet kvarstår

---

## 📄 Licens & Användning

Denna frågegenerator är skapad för utbildningssyfte. Använd den fritt för dina klasser!

**Kom ihåg:**
- Granska alltid AI-genererade frågor
- AI är ett verktyg som hjälper dig, inte ersätter dig
- Din pedagogiska expertis är ovärderlig för att skapa bra quiz

---

**Lycka till med dina quiz! 🎉**
