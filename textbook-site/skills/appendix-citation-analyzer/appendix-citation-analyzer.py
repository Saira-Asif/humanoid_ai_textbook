#!/usr/bin/env python3
"""
Appendix Citation Analyzer
Specialized analyzer for citations in appendix sections of documents.
Focuses on verifying proper formatting and cross-references within appendices.
Used in Phase 4 (Quality Assurance) of the textbook project for appendix validation.
"""

import argparse
import re
import sys
from typing import List, Dict, Tuple


def analyze_appendix_citations(text: str) -> Dict:
    """
    Analyze citations specifically in appendix sections of text.

    Args:
        text: Input text to analyze (specifically appendix content)

    Returns:
        Dictionary containing analysis results
    """
    # Find appendix sections
    appendix_sections = _extract_appendix_sections(text)

    results = {
        'appendix_count': len(appendix_sections),
        'section_analysis': [],
        'cross_reference_issues': [],
        'formatting_issues': []
    }

    for i, (section_title, content) in enumerate(appendix_sections):
        section_analysis = {
            'section': section_title,
            'citations': [],
            'figures_tables': [],
            'cross_references': []
        }

        # Find citations in appendix
        citations = _find_citations(content)
        section_analysis['citations'] = citations

        # Find figures and tables references
        fig_table_refs = _find_figure_table_references(content)
        section_analysis['figures_tables'] = fig_table_refs

        # Find cross-references within appendix
        cross_refs = _find_cross_references(content)
        section_analysis['cross_references'] = cross_refs

        # Validate formatting
        formatting_issues = _check_formatting(content)
        results['formatting_issues'].extend([
            f"{section_title}: {issue}" for issue in formatting_issues
        ])

        # Validate cross-references
        cross_ref_issues = _validate_cross_references(content, cross_refs)
        results['cross_reference_issues'].extend([
            f"{section_title}: {issue}" for issue in cross_ref_issues
        ])

        results['section_analysis'].append(section_analysis)

    return results


def _extract_appendix_sections(text: str) -> List[Tuple[str, str]]:
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


def _find_citations(text: str) -> List[str]:
    """Find citations in text."""
    citation_patterns = [
        r'\[([A-Za-z0-9,.\-\s]+)\]',  # [Author, Year] or [1, 2, 3]
        r'\(([A-Za-z0-9,\s]+;\s[A-Za-z0-9,\s]+)\)',  # (Author, Year; Author, Year)
        r'([A-Za-z]+,\s[0-9]{4})',  # Author, Year
    ]

    citations = []
    for pattern in citation_patterns:
        matches = re.findall(pattern, text)
        citations.extend(matches)

    # Remove duplicates while preserving order
    seen = set()
    unique_citations = []
    for cit in citations:
        if cit not in seen:
            seen.add(cit)
            unique_citations.append(cit)

    return unique_citations


def _find_figure_table_references(text: str) -> List[str]:
    """Find figure and table references in text."""
    fig_table_patterns = [
        r'(Figure\s+\d+[A-Z]?)',  # Figure 1, Figure 1A
        r'(Table\s+\d+[A-Z]?)',   # Table 1, Table 1A
        r'(Fig\.\s+\d+[A-Z]?)',   # Fig. 1, Fig. 1A
    ]

    references = []
    for pattern in fig_table_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        references.extend(matches)

    # Remove duplicates while preserving order
    seen = set()
    unique_refs = []
    for ref in references:
        if ref.lower() not in [x.lower() for x in unique_refs]:
            seen.add(ref.lower())
            unique_refs.append(ref)

    return unique_refs


def _find_cross_references(text: str) -> List[str]:
    """Find cross-references within appendix."""
    cross_ref_patterns = [
        r'(Section\s+\d+[A-Z]?)',  # Section 1, Section 1A
        r'(Appendix\s+[A-Z\d]+)',  # Appendix A, Appendix B
        r'(Chapter\s+\d+)',        # Chapter 1
        r'(page\s+\d+)',           # page 10
    ]

    references = []
    for pattern in cross_ref_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        references.extend(matches)

    # Remove duplicates while preserving order
    seen = set()
    unique_refs = []
    for ref in references:
        if ref.lower() not in [x.lower() for x in unique_refs]:
            seen.add(ref.lower())
            unique_refs.append(ref)

    return unique_refs


def _check_formatting(text: str) -> List[str]:
    """Check for common formatting issues in appendix."""
    issues = []

    # Check for missing headers
    if not re.search(r'^\s*[A-Z][^:.]*:', text, re.MULTILINE):
        issues.append("Possible missing header structure")

    # Check for inconsistent spacing
    if re.search(r'\n\s*\n\s*\n', text):  # Multiple blank lines
        issues.append("Multiple consecutive blank lines detected")

    return issues


def _validate_cross_references(text: str, cross_refs: List[str]) -> List[str]:
    """Validate cross-references point to existing elements."""
    issues = []

    for ref in cross_refs:
        # Check if referenced element exists in the text
        if ref.lower().startswith('section'):
            # Look for the section in the text
            section_num = re.search(r'\d+[A-Z]?', ref)
            if section_num:
                expected_header = rf'^\s*Section\s+{section_num.group()}'
                if not re.search(expected_header, text, re.MULTILINE | re.IGNORECASE):
                    issues.append(f"Cross-reference to non-existent {ref}")

        elif ref.lower().startswith('appendix'):
            # Look for the appendix in the text
            appendix_id = re.search(r'[A-Z\d]+', ref)
            if appendix_id:
                expected_header = rf'^\s*Appendix\s+{appendix_id.group()}'
                if not re.search(expected_header, text, re.MULTILINE | re.IGNORECASE):
                    issues.append(f"Cross-reference to non-existent {ref}")

    return issues


def main():
    parser = argparse.ArgumentParser(description='Analyze citations in appendix sections')
    parser.add_argument('input_file', help='Input text file containing appendix content')
    parser.add_argument('-o', '--output', help='Output file for results (default: stdout)')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            text = f.read()

        results = analyze_appendix_citations(text)

        output = sys.stdout
        if args.output:
            output = open(args.output, 'w', encoding='utf-8')

        output.write("Appendix Citation Analysis Results:\n")
        output.write(f"Number of appendices analyzed: {results['appendix_count']}\n\n")

        for section_analysis in results['section_analysis']:
            output.write(f"Section: {section_analysis['section']}\n")
            output.write(f"  Citations found: {len(section_analysis['citations'])}\n")
            output.write(f"  Figure/Table references: {len(section_analysis['figures_tables'])}\n")
            output.write(f"  Cross-references: {len(section_analysis['cross_references'])}\n\n")

        if results['cross_reference_issues']:
            output.write("Cross-reference issues:\n")
            for issue in results['cross_reference_issues']:
                output.write(f"- {issue}\n")
            output.write("\n")

        if results['formatting_issues']:
            output.write("Formatting issues:\n")
            for issue in results['formatting_issues']:
                output.write(f"- {issue}\n")

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