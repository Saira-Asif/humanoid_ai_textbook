#!/usr/bin/env python3
"""
Active Voice Analyzer
Analyzes text documents to identify passive voice constructions and suggests active voice alternatives.
Used in Phase 4 (Quality Assurance) of the textbook project to improve clarity and engagement.
"""

import argparse
import re
import sys
from typing import List, Tuple


def find_passive_voice(text: str) -> List[Tuple[int, str, str]]:
    """
    Find passive voice constructions in text and suggest active alternatives.

    Args:
        text: Input text to analyze

    Returns:
        List of tuples containing (line_number, passive_phrase, suggested_active_alternative)
    """
    # Common passive voice patterns
    passive_patterns = [
        r'\b(am|is|are|was|were|be|being|been)\s+\w+ed\b',
        r'\b(am|is|are|was|were|be|being|been)\s+\w+n\b',  # past participle ending in 'n'
        r'\b(am|is|are|was|were|be|being|been)\s+\w+en\b', # past participle ending in 'en'
    ]

    results = []
    lines = text.split('\n')

    for line_num, line in enumerate(lines, 1):
        for pattern in passive_patterns:
            matches = re.finditer(pattern, line, re.IGNORECASE)
            for match in matches:
                passive_phrase = match.group(0)
                # Simple suggestion (in practice, this would be more sophisticated)
                suggested_active = _suggest_active_alternative(passive_phrase)
                results.append((line_num, passive_phrase.strip(), suggested_active))

    return results


def _suggest_active_alternative(passive_phrase: str) -> str:
    """Simple function to suggest active voice alternative."""
    # This is a simplified version - real implementation would be more complex
    return f"[ACTIVE VOICE SUGGESTION FOR: {passive_phrase}]"


def main():
    parser = argparse.ArgumentParser(description='Analyze text for passive voice constructions')
    parser.add_argument('input_file', help='Input text file to analyze')
    parser.add_argument('-o', '--output', help='Output file for results (default: stdout)')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            text = f.read()

        results = find_passive_voice(text)

        output = sys.stdout
        if args.output:
            output = open(args.output, 'w', encoding='utf-8')

        if results:
            output.write(f"Found {len(results)} passive voice constructions:\n")
            for line_num, passive, active_suggestion in results:
                output.write(f"Line {line_num}: '{passive}' -> {active_suggestion}\n")
        else:
            output.write("No passive voice constructions found.\n")

        if args.output:
            output.close()

    except FileNotFoundError:
        print(f"Error: File '{args.input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()