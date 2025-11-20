#!/usr/bin/env python3
"""
Frågegenerator-agent för Retrieval Övningsapplikation

Denna agent genererar automatiskt 1X2-frågor från textavsnitt.
Den skapar frågor med tre svarsalternativ och ett rätt svar.
"""

import os
import sys
import json
import argparse
from typing import List, Dict

def generate_questions_prompt(text: str, num_questions: int, subject: str = "Historia") -> str:
    """Skapa prompt för att generera frågor"""
    return f"""Du är en expert på att skapa pedagogiska övningsfrågor för {subject}.

Din uppgift är att skapa {num_questions} st 1X2-frågor (flervalsfrågorfrågor) från följande text.

VIKTIGA REGLER:
1. Skapa frågor som testar faktakunskap och förståelse
2. Varje fråga ska ha EXAKT 3 svarsalternativ
3. Endast ETT alternativ är rätt
4. De två felaktiga alternativen (distraktorer) ska vara trovärdiga men tydligt felaktiga
5. Frågorna ska vara på svenska
6. Svara ENDAST med JSON-format (inget annat text)

TEXT:
{text}

Svara med följande JSON-format:
{{
  "questions": [
    {{
      "question": "Frågetexten här?",
      "option1": "Första alternativet",
      "option2": "Andra alternativet",
      "option3": "Tredje alternativet",
      "correct": 1
    }}
  ]
}}

Där "correct" är 1, 2 eller 3 (vilket alternativ som är rätt).

Generera {num_questions} frågor nu:"""


def parse_questions_response(response: str) -> List[Dict]:
    """Parse AI-svar och extrahera frågor"""
    try:
        # Försök hitta JSON i svaret
        start = response.find('{')
        end = response.rfind('}') + 1

        if start == -1 or end == 0:
            raise ValueError("Kunde inte hitta JSON i svaret")

        json_str = response[start:end]
        data = json.loads(json_str)

        return data.get('questions', [])
    except Exception as e:
        print(f"Fel vid parsning av svar: {e}")
        print(f"Svar: {response}")
        return []


def questions_to_csv(questions: List[Dict]) -> str:
    """Konvertera frågor till CSV-format"""
    csv_lines = []

    for q in questions:
        question = q.get('question', '').strip()
        option1 = q.get('option1', '').strip()
        option2 = q.get('option2', '').strip()
        option3 = q.get('option3', '').strip()
        correct = q.get('correct', 1)

        # Escape kommatecken i text
        question = question.replace(',', ';')
        option1 = option1.replace(',', ';')
        option2 = option2.replace(',', ';')
        option3 = option3.replace(',', ';')

        csv_line = f'"{question}","{option1}","{option2}","{option3}",{correct}'
        csv_lines.append(csv_line)

    return '\n'.join(csv_lines)


def generate_with_anthropic(text: str, num_questions: int, subject: str, api_key: str) -> List[Dict]:
    """Generera frågor med Anthropic Claude API"""
    try:
        import anthropic
    except ImportError:
        print("Fel: 'anthropic' paketet är inte installerat.")
        print("Installera det med: pip install anthropic")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    prompt = generate_questions_prompt(text, num_questions, subject)

    print("Genererar frågor med Claude AI...")

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response_text = message.content[0].text
    questions = parse_questions_response(response_text)

    return questions


def generate_with_openai(text: str, num_questions: int, subject: str, api_key: str) -> List[Dict]:
    """Generera frågor med OpenAI GPT API"""
    try:
        from openai import OpenAI
    except ImportError:
        print("Fel: 'openai' paketet är inte installerat.")
        print("Installera det med: pip install openai")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    prompt = generate_questions_prompt(text, num_questions, subject)

    print("Genererar frågor med OpenAI GPT...")

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Du är en expert på att skapa pedagogiska övningsfrågor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    response_text = response.choices[0].message.content
    questions = parse_questions_response(response_text)

    return questions


def main():
    parser = argparse.ArgumentParser(
        description='Generera 1X2-frågor från text med AI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exempel:
  python fragegenerator.py --input text.txt --output fragor.csv --num 10
  python fragegenerator.py --text "Sverige blev medlem i EU 1995" --num 3
  python fragegenerator.py --input historia.txt --subject "Historia" --api anthropic
        """
    )

    # Input options
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('--input', '-i', help='Textfil att läsa från')
    input_group.add_argument('--text', '-t', help='Text direkt som argument')

    # Output options
    parser.add_argument('--output', '-o', default='genererade_fragor.csv',
                        help='Output CSV-fil (default: genererade_fragor.csv)')

    # Generation options
    parser.add_argument('--num', '-n', type=int, default=5,
                        help='Antal frågor att generera (default: 5)')
    parser.add_argument('--subject', '-s', default='Historia',
                        help='Ämne (default: Historia)')

    # API options
    parser.add_argument('--api', choices=['anthropic', 'openai'], default='anthropic',
                        help='Vilket AI API att använda (default: anthropic)')
    parser.add_argument('--api-key', help='API-nyckel (eller sätt ANTHROPIC_API_KEY / OPENAI_API_KEY)')

    args = parser.parse_args()

    # Get text
    if args.input:
        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                text = f.read()
            print(f"Läste text från: {args.input}")
        except Exception as e:
            print(f"Fel vid läsning av fil: {e}")
            sys.exit(1)
    else:
        text = args.text

    if not text.strip():
        print("Fel: Ingen text angiven")
        sys.exit(1)

    # Get API key
    api_key = args.api_key
    if not api_key:
        if args.api == 'anthropic':
            api_key = os.getenv('ANTHROPIC_API_KEY')
            if not api_key:
                print("Fel: ANTHROPIC_API_KEY saknas")
                print("Sätt miljövariabeln eller använd --api-key")
                sys.exit(1)
        else:
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                print("Fel: OPENAI_API_KEY saknas")
                print("Sätt miljövariabeln eller använd --api-key")
                sys.exit(1)

    # Generate questions
    try:
        if args.api == 'anthropic':
            questions = generate_with_anthropic(text, args.num, args.subject, api_key)
        else:
            questions = generate_with_openai(text, args.num, args.subject, api_key)

        if not questions:
            print("Fel: Inga frågor genererades")
            sys.exit(1)

        print(f"\n✓ Genererade {len(questions)} frågor")

        # Convert to CSV
        csv_content = questions_to_csv(questions)

        # Save to file
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(csv_content)

        print(f"✓ Sparade frågor till: {args.output}")

        # Preview
        print("\nFörhandsvisning av första frågan:")
        print("-" * 50)
        if questions:
            q = questions[0]
            print(f"Fråga: {q.get('question')}")
            print(f"1. {q.get('option1')}")
            print(f"2. {q.get('option2')}")
            print(f"3. {q.get('option3')}")
            print(f"Rätt svar: {q.get('correct')}")

    except Exception as e:
        print(f"Fel vid generering: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
