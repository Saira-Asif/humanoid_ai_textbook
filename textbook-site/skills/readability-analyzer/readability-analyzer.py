#!/usr/bin/env python3
"""
Readability Analyzer
Calculates various readability metrics including Flesch-Kincaid Grade Level,
Flesch Reading Ease, and other text complexity measures.
Used in Phase 4 (Quality Assurance) of the textbook project to ensure appropriate reading level.
"""

import argparse
import re
import sys
from typing import Dict, List
import math


def calculate_readability_metrics(text: str) -> Dict:
    """
    Calculate various readability metrics for the given text.

    Args:
        text: Input text to analyze

    Returns:
        Dictionary containing readability metrics
    """
    # Clean the text
    clean_text = _clean_text(text)

    # Count sentences, words, and syllables
    sentences = _count_sentences(clean_text)
    words = _count_words(clean_text)
    syllables = _count_syllables(clean_text)

    # Calculate readability scores
    metrics = {}

    if sentences > 0 and words > 0:
        # Flesch Reading Ease Score
        # 206.835 - (1.015 × (total words / total sentences)) - (84.6 × (total syllables / total words))
        if words > 0:
            avg_words_per_sentence = words / sentences
            avg_syllables_per_word = syllables / words
            flesch_ease = 206.835 - (1.015 * avg_words_per_sentence) - (84.6 * avg_syllables_per_word)
            metrics['flesch_reading_ease'] = round(flesch_ease, 2)

            # Determine difficulty level
            if flesch_ease >= 90:
                metrics['ease_level'] = 'Very Easy'
            elif flesch_ease >= 80:
                metrics['ease_level'] = 'Easy'
            elif flesch_ease >= 70:
                metrics['ease_level'] = 'Fairly Easy'
            elif flesch_ease >= 60:
                metrics['ease_level'] = 'Standard'
            elif flesch_ease >= 50:
                metrics['ease_level'] = 'Fairly Difficult'
            elif flesch_ease >= 30:
                metrics['ease_level'] = 'Difficult'
            else:
                metrics['ease_level'] = 'Very Confusing'
        else:
            metrics['flesch_reading_ease'] = 0
            metrics['ease_level'] = 'N/A'

        # Flesch-Kincaid Grade Level
        # (0.39 × (total words / total sentences)) + (11.8 × (total syllables / total words)) - 15.59
        if words > 0:
            fk_grade = (0.39 * avg_words_per_sentence) + (11.8 * avg_syllables_per_word) - 15.59
            metrics['flesch_kincaid_grade'] = round(fk_grade, 2)
        else:
            metrics['flesch_kincaid_grade'] = 0

        # Additional metrics
        metrics['sentences'] = sentences
        metrics['words'] = words
        metrics['syllables'] = syllables
        metrics['avg_words_per_sentence'] = round(words / sentences, 2) if sentences > 0 else 0
        metrics['avg_syllables_per_word'] = round(syllables / words, 2) if words > 0 else 0

        # Automated Readability Index (ARI)
        # 4.71 * (characters/words) + 0.5 * (words/sentences) - 21.43
        characters = len(re.sub(r'\s', '', clean_text))
        if words > 0 and sentences > 0:
            ari = 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43
            metrics['automated_readability_index'] = round(ari, 2)
        else:
            metrics['automated_readability_index'] = 0

    return metrics


def _clean_text(text: str) -> str:
    """Clean text by removing special formatting while preserving content."""
    # Remove special formatting but keep basic punctuation
    clean = re.sub(r'<[^>]+>', ' ', text)  # Remove HTML tags
    clean = re.sub(r'\[[0-9]+\]', ' ', text)  # Remove citation brackets
    return clean


def _count_sentences(text: str) -> int:
    """Count number of sentences in text."""
    # Split on sentence-ending punctuation
    sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings
    return len([s for s in sentences if s.strip()])


def _count_words(text: str) -> int:
    """Count number of words in text."""
    # Find all word-like sequences
    words = re.findall(r'\b\w+\b', text)
    return len(words)


def _count_syllables(text: str) -> int:
    """Count number of syllables in text."""
    words = re.findall(r'\b\w+\b', text)
    total_syllables = 0

    for word in words:
        syllables = _count_syllables_in_word(word.lower())
        total_syllables += syllables

    return total_syllables


def _count_syllables_in_word(word: str) -> int:
    """Count syllables in a single word using vowel group counting."""
    # Remove trailing 'e' if it's not the only vowel (for silent e)
    if word.endswith('e') and len(word) > 1:
        vowels = 'aeiouy'
        vowel_groups = 0
        prev_was_vowel = False

        for char in word[:-1]:  # exclude the last 'e'
            is_vowel = char in vowels
            if is_vowel and not prev_was_vowel:
                vowel_groups += 1
            prev_was_vowel = is_vowel

        # If the word ends with 'e' and we found vowel groups, add one syllable
        if vowel_groups == 0:
            # Handle words like "the", "me" that are typically 1 syllable
            return 1
        else:
            # If the original word had 'e' at the end, add a syllable unless it creates a break
            if vowel_groups > 0:
                return max(vowel_groups, 1)
            else:
                return 1
    else:
        # Count vowel groups in the whole word
        vowels = 'aeiouy'
        vowel_groups = 0
        prev_was_vowel = False

        for char in word:
            is_vowel = char in vowels
            if is_vowel and not prev_was_vowel:
                vowel_groups += 1
            prev_was_vowel = is_vowel

        return max(vowel_groups, 1)


def main():
    parser = argparse.ArgumentParser(description='Analyze text readability metrics')
    parser.add_argument('input_file', help='Input text file to analyze')
    parser.add_argument('-o', '--output', help='Output file for results (default: stdout)')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            text = f.read()

        metrics = calculate_readability_metrics(text)

        output = sys.stdout
        if args.output:
            output = open(args.output, 'w', encoding='utf-8')

        output.write("Readability Analysis Results:\n")
        output.write(f"Flesch Reading Ease: {metrics.get('flesch_reading_ease', 0)} ({metrics.get('ease_level', 'N/A')})\n")
        output.write(f"Flesch-Kincaid Grade Level: {metrics.get('flesch_kincaid_grade', 0)}\n")
        output.write(f"Automated Readability Index: {metrics.get('automated_readability_index', 0)}\n")
        output.write(f"Total Sentences: {metrics.get('sentences', 0)}\n")
        output.write(f"Total Words: {metrics.get('words', 0)}\n")
        output.write(f"Total Syllables: {metrics.get('syllables', 0)}\n")
        output.write(f"Avg Words per Sentence: {metrics.get('avg_words_per_sentence', 0)}\n")
        output.write(f"Avg Syllables per Word: {metrics.get('avg_syllables_per_word', 0)}\n")

        # Target grade level assessment
        fk_grade = metrics.get('flesch_kincaid_grade', 0)
        if 12 <= fk_grade <= 14:
            output.write(f"\n✅ Target grade level achieved: {fk_grade:.1f} (within 12-14 range)\n")
        else:
            output.write(f"\n❌ Grade level outside target range: {fk_grade:.1f} (target: 12-14)\n")

        if args.output:
            output.close()

    except FileNotFoundError as e:
        print(f"Error: File not found - {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()