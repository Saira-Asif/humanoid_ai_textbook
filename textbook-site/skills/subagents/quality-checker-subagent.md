# Quality Checker Subagent

## Definition

The Quality Checker Subagent is a composite AI agent that combines all six quality assurance skills into a single, cohesive quality validation pipeline. This subagent provides a unified interface for executing comprehensive quality checks on technical documentation, applying all validation rules simultaneously for efficient processing.

## Claude Code Prompt Template

Use this template to invoke the Quality Checker Subagent in Claude Code:

```
You are a Quality Checker Subagent that performs comprehensive quality validation on technical documentation. Execute the following quality checks:

1. Active Voice Analysis:
   - Run active-voice-analyzer on the provided content
   - Target: >98% active voice usage
   - Report passive voice constructions that need attention

2. Citation Analysis:
   - Run citation-analyzer to validate citations and references
   - Target: 100% citation-reference alignment
   - Report missing or invalid citations

3. Appendix Citation Analysis (if applicable):
   - Run appendix-citation-analyzer on appendix sections
   - Validate appendix-specific citations and cross-references
   - Report any cross-reference issues

4. Readability Analysis:
   - Run readability-analyzer to assess reading level
   - Target: Grade 12-14 Flesch-Kincaid level
   - Report if content falls outside target range

5. Appendix Readability Analysis (if applicable):
   - Run appendix-readability-analyzer on appendix content
   - Validate appendix readability metrics
   - Report technical complexity issues

6. Content Simplification (if needed):
   - Run simplify-content to improve clarity
   - Preserve technical accuracy while improving readability
   - Suggest simplifications for complex passages

Execute these checks in sequence and provide a comprehensive quality report with specific recommendations for improvement.
```

## Usage Instructions

### Single Command Quality Check
```bash
# Create a script that runs all quality checks
./quality-checker.sh input_document.txt

# Or execute sequentially:
python active-voice-analyzer/active-voice-analyzer.py input.txt -o results/active_voice.txt
python citation-analyzer/citation-analyzer.py input.txt -r references.txt -o results/citations.txt
python readability-analyzer/readability-analyzer.py input.txt -o results/readability.txt
# ... continue for all analyzers
```

### Claude Code Integration
1. Load the prompt template above into Claude Code
2. Provide the document content for analysis
3. Review the comprehensive quality report
4. Implement suggested improvements
5. Re-run validation to confirm fixes

## Example Workflow

```
USER: Please run a comprehensive quality check on this textbook chapter.

CLAUDE (as Quality Checker Subagent):
Running comprehensive quality analysis...

1. Active Voice Analysis:
   - Found 2 passive constructions in lines 15, 28
   - Current active voice rate: 97.8% (Target: >98%)
   - Suggestions provided for improvement

2. Citation Analysis:
   - 18 citations found, 100% reference coverage
   - No citation-reference mismatches detected

3. Readability Analysis:
   - Flesch-Kincaid Grade Level: 13.4 (Target: 12-14) ✅
   - Flesch Reading Ease: 42.1 (Fairly Difficult)

4. Content Simplification Suggestions:
   - Longest sentence: 32 words in line 45
   - Complex term "utilization" found 7 times, suggest "use"

Overall: Document meets quality standards with minor improvements needed for active voice.
```

## Expected Outputs

The Quality Checker Subagent produces a comprehensive report including:

### 📊 Summary Dashboard
- Active voice percentage
- Citation coverage rate
- Readability grade level
- Technical complexity indicators

### 📝 Detailed Analysis
- Line-by-line issues from each analyzer
- Specific improvement recommendations
- Priority ranking of required changes

### 🎯 Compliance Status
- Pass/fail status for each quality metric
- Areas requiring immediate attention
- Suggestions for maintaining standards

## Integration Benefits

- **Efficiency**: Execute all quality checks in a single pass
- **Consistency**: Apply uniform standards across all validation steps
- **Comprehensiveness**: Catch issues that individual checks might miss
- **Time Savings**: Reduce manual quality assurance from hours to minutes
- **Standardization**: Ensure all content meets the same quality benchmarks

## Quality Assurance Pipeline Position

The Quality Checker Subagent fits into the validation pipeline after initial content creation and before final review, ensuring all content meets the established quality standards before human review.