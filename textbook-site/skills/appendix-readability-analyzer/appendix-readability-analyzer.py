#!/usr/bin/env python3
"""
Appendix Readability Analyzer
Specialized readability analyzer for appendix sections of documents.
Calculates readability metrics specifically tailored for technical appendices.
Used in Phase 4 (Quality Assurance) of the textbook project for appendix content validation.
"""

import argparse
import re
import sys
from typing import Dict, List
import math


def calculate_appendix_readability_metrics(text: str) -> Dict:
    """
    Calculate readability metrics specifically for appendix sections.

    Args:
        text: Input text to analyze (specifically appendix content)

    Returns:
        Dictionary containing appendix-specific readability metrics
    """
    # Extract appendix sections
    appendix_sections = _extract_appendix_sections(text)

    results = {
        'appendix_count': len(appendix_sections),
        'overall_metrics': {},
        'section_metrics': [],
        'technical_complexity_indicators': []
    }

    all_sentences = 0
    all_words = 0
    all_syllables = 0
    all_characters = 0

    for i, (section_title, content) in enumerate(appendix_sections):
        section_metrics = calculate_readability_metrics(content)
        section_metrics['section_title'] = section_title

        # Analyze technical complexity indicators
        tech_indicators = _analyze_technical_complexity(content)
        section_metrics['technical_indicators'] = tech_indicators

        results['section_metrics'].append(section_metrics)

        # Accumulate for overall calculation
        all_sentences += section_metrics.get('sentences', 0)
        all_words += section_metrics.get('words', 0)
        all_syllables += section_metrics.get('syllables', 0)

        # Count characters for ARI calculation
        clean_content = _clean_text(content)
        all_characters += len(re.sub(r'\s', '', clean_content))

    # Calculate overall metrics if we have content
    if all_words > 0 and all_sentences > 0:
        # Overall Flesch Reading Ease
        avg_words_per_sentence = all_words / all_sentences
        avg_syllables_per_word = all_syllables / all_words
        flesch_ease = 206.835 - (1.015 * avg_words_per_sentence) - (84.6 * avg_syllables_per_word)
        results['overall_metrics']['flesch_reading_ease'] = round(flesch_ease, 2)

        # Overall Flesch-Kincaid Grade Level
        fk_grade = (0.39 * avg_words_per_sentence) + (11.8 * avg_syllables_per_word) - 15.59
        results['overall_metrics']['flesch_kincaid_grade'] = round(fk_grade, 2)

        # Overall Automated Readability Index
        ari = 4.71 * (all_characters / all_words) + 0.5 * (all_words / all_sentences) - 21.43
        results['overall_metrics']['automated_readability_index'] = round(ari, 2)

        results['overall_metrics']['sentences'] = all_sentences
        results['overall_metrics']['words'] = all_words
        results['overall_metrics']['syllables'] = all_syllables

    # Analyze overall technical complexity
    results['technical_complexity_indicators'] = _analyze_overall_technical_complexity(text)

    return results


def _extract_appendix_sections(text: str) -> List[tuple]:
    """Extract appendix sections from text."""
    # Look for Appendix patterns
    appendix_pattern = r'(Appendix\s+[A-Z\d]+[^\n]*\n)(.*?)(?=\nAppendix\s+[A-Z\d]+|\Z)'
    matches = re.findall(appendix_pattern, text, re.DOTALL | re.IGNORECASE)

    sections = []
    for match in matches:
        title = match[0].strip()
        content = match[1].strip()
        sections.append((title, content))

    return sections


def calculate_readability_metrics(text: str) -> Dict:
    """Calculate standard readability metrics."""
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

        # Flesch-Kincaid Grade Level
        fk_grade = (0.39 * avg_words_per_sentence) + (11.8 * avg_syllables_per_word) - 15.59
        metrics['flesch_kincaid_grade'] = round(fk_grade, 2)

        # Additional metrics
        metrics['sentences'] = sentences
        metrics['words'] = words
        metrics['syllables'] = syllables
        metrics['avg_words_per_sentence'] = round(avg_words_per_sentence, 2)
        metrics['avg_syllables_per_word'] = round(avg_syllables_per_word, 2)

        # Automated Readability Index (ARI)
        characters = len(re.sub(r'\s', '', clean_text))
        ari = 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43
        metrics['automated_readability_index'] = round(ari, 2)

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


def _analyze_technical_complexity(text: str) -> Dict:
    """Analyze technical complexity indicators in appendix text."""
    indicators = {
        'complex_words': [],  # Long words (>7 syllables)
        'jargon_terms': [],   # Potential jargon (acronyms, technical terms)
        'mathematical_expressions': 0,  # Number of math expressions
        'specialized_vocabulary_density': 0.0  # Ratio of technical terms to total words
    }

    # Find long words (potential complex terms)
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        syllables = _count_syllables_in_word(word.lower())
        if syllables > 3:  # Consider words with more than 3 syllables as complex
            indicators['complex_words'].append(word)

    # Find acronyms and potential jargon
    acronyms = re.findall(r'\b[A-Z]{2,}\b', text)
    indicators['jargon_terms'].extend(acronyms)

    # Find mathematical expressions
    math_patterns = [
        r'\$\$.+?\$\$',  # LaTeX inline math
        r'\$.+?\$',      # LaTeX display math
        r'[0-9]+[+\-*/=][0-9]+',  # Simple equations
        r'∑|∏|∫|∂|∇|∞|≠|≤|≥|±',  # Mathematical symbols
    ]
    math_count = 0
    for pattern in math_patterns:
        matches = re.findall(pattern, text)
        math_count += len(matches)
    indicators['mathematical_expressions'] = math_count

    # Calculate density
    if len(words) > 0:
        indicators['specialized_vocabulary_density'] = len(indicators['complex_words']) / len(words)

    return indicators


def _analyze_overall_technical_complexity(text: str) -> List[str]:
    """Analyze overall technical complexity indicators."""
    issues = []

    # Check if the text has too high a density of complex words
    words = re.findall(r'\b\w+\b', text)
    if len(words) > 0:
        complex_words = []
        for word in words:
            if _count_syllables_in_word(word.lower()) > 3:
                complex_words.append(word)

        density = len(complex_words) / len(words)
        if density > 0.25:  # More than 25% complex words
            issues.append("High density of complex words (>25%) - may affect readability")

    # Check for excessive technical jargon
    acronyms = re.findall(r'\b[A-Z]{2,}\b', text)
    if len(acronyms) / len(words) > 0.05:  # More than 5% acronyms
        issues.append("High frequency of acronyms (>5%) - consider defining terms")

    return issues


def main():
    parser = argparse.ArgumentParser(description='Analyze readability of appendix sections')
    parser.add_argument('input_file', help='Input text file containing appendix content')
    parser.add_argument('-o', '--output', help='Output file for results (default: stdout)')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            text = f.read()

        results = calculate_appendix_readability_metrics(text)

        output = sys.stdout
        if args.output:
            output = open(args.output, 'w', encoding='utf-8')

        output.write("Appendix Readability Analysis Results:\n")
        output.write(f"Number of appendices analyzed: {results['appendix_count']}\n\n")

        # Overall metrics
        overall = results['overall_metrics']
        if overall:
            output.write("Overall Metrics:\n")
            output.write(f"  Flesch Reading Ease: {overall.get('flesch_reading_ease', 0)}\n")
            output.write(f"  Flesch-Kincaid Grade Level: {overall.get('flesch_kincaid_grade', 0)}\n")
            output.write(f"  Automated Readability Index: {overall.get('automated_readability_index', 0)}\n")
            output.write(f"  Total Words: {overall.get('words', 0)}\n")
            output.write("\n")

        # Section-specific metrics
        for section_data in results['section_metrics']:
            output.write(f"Section: {section_data['section_title']}\n")
            output.write(f"  Flesch-Kincaid Grade Level: {section_data.get('flesch_kincaid_grade', 0)}\n")
            output.write(f"  Words: {section_data.get('words', 0)}\n")

            # Technical indicators
            tech = section_data.get('technical_indicators', {})
            if tech.get('complex_words'):
                output.write(f"  Complex words (>3 syllables): {len(tech['complex_words'])}\n")
            if tech.get('jargon_terms'):
                output.write(f"  Acronyms/Technical terms: {len(tech['jargon_terms'])}\n")
            output.write(f"  Math expressions: {tech.get('mathematical_expressions', 0)}\n")
            output.write("\n")

        # Technical complexity issues
        if results['technical_complexity_indicators']:
            output.write("Technical Complexity Issues:\n")
            for issue in results['technical_complexity_indicators']:
                output.write(f"  - {issue}\n")

        # Target grade level assessment
        fk_grade = overall.get('flesch_kincaid_grade', 0)
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