#!/usr/bin/env python3
"""
Citation Analyzer
Analyzes text documents to verify proper citation formatting and coverage.
Checks for missing citations, incorrect formats, and validates reference list completeness.
Used in Phase 4 (Quality Assurance) of the textbook project to ensure academic integrity.
"""

import argparse
import re
import sys
from typing import List, Dict, Tuple


def analyze_citations(text: str, reference_list: str = None) -> Dict:
    """
    Analyze citations in text and check against reference list if provided.

    Args:
        text: Input text to analyze
        reference_list: Optional reference list to validate against

    Returns:
        Dictionary containing analysis results
    """
    # Find in-text citations (common academic formats)
    citation_patterns = [
        r'\[([A-Za-z0-9,.\-\s]+)\]',  # [Author, Year] or [1, 2, 3]
        r'\(([A-Za-z0-9,\s]+;\s[A-Za-z0-9,\s]+)\)',  # (Author, Year; Author, Year)
        r'([A-Za-z]+,\s[0-9]{4})',  # Author, Year
        r'([A-Za-z]+\s\[et al\.,\s[0-9]{4}\])',  # Author et al., Year
    ]

    found_citations = []
    lines = text.split('\n')

    for line_num, line in enumerate(lines, 1):
        for pattern in citation_patterns:
            matches = re.finditer(pattern, line)
            for match in matches:
                citation = match.group(0).strip()
                if citation not in found_citations:
                    found_citations.append(citation)

    # Check for common citation issues
    issues = []
    for citation in found_citations:
        if not _validate_citation_format(citation):
            issues.append(f"Invalid format: {citation}")

    return {
        'total_citations': len(found_citations),
        'citations_found': found_citations,
        'issues': issues,
        'reference_validation': _validate_references(found_citations, reference_list) if reference_list else {}
    }


def _validate_citation_format(citation: str) -> bool:
    """Validate citation format."""
    # Simple validation - in practice this would be more comprehensive
    return len(citation) > 3  # Basic check


def _validate_references(citations: List[str], reference_list: str) -> Dict:
    """Validate citations against reference list."""
    if not reference_list:
        return {}

    # Extract reference identifiers from reference list
    refs = re.findall(r'\[?([A-Za-z0-9]+)\]?', reference_list)
    cited_refs = []

    for citation in citations:
        # Extract reference keys from citations
        keys = re.findall(r'[A-Za-z0-9]+', citation)
        cited_refs.extend(keys)

    missing_from_refs = set(cited_refs) - set(refs)
    unused_refs = set(refs) - set(cited_refs)

    return {
        'missing_from_references': list(missing_from_refs),
        'unused_references': list(unused_refs),
        'coverage_percentage': (len(set(cited_refs)) / max(len(set(refs)), 1)) * 100
    }


def main():
    parser = argparse.ArgumentParser(description='Analyze citations in text documents')
    parser.add_argument('input_file', help='Input text file to analyze')
    parser.add_argument('-r', '--references', help='Reference list file to validate against')
    parser.add_argument('-o', '--output', help='Output file for results (default: stdout)')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            text = f.read()

        reference_list = None
        if args.references:
            with open(args.references, 'r', encoding='utf-8') as f:
                reference_list = f.read()

        results = analyze_citations(text, reference_list)

        output = sys.stdout
        if args.output:
            output = open(args.output, 'w', encoding='utf-8')

        output.write("Citation Analysis Results:\n")
        output.write(f"Total citations found: {results['total_citations']}\n")

        if results['issues']:
            output.write("\nIssues found:\n")
            for issue in results['issues']:
                output.write(f"- {issue}\n")

        if results['reference_validation']:
            ref_results = results['reference_validation']
            output.write(f"\nReference validation:\n")
            output.write(f"Coverage: {ref_results.get('coverage_percentage', 0):.1f}%\n")

            if ref_results.get('missing_from_references'):
                output.write("Missing from reference list:\n")
                for ref in ref_results['missing_from_references']:
                    output.write(f"- {ref}\n")

            if ref_results.get('unused_references'):
                output.write("Unused references:\n")
                for ref in ref_results['unused_references']:
                    output.write(f"- {ref}\n")

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