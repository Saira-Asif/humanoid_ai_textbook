#!/usr/bin/env python3
"""
Simplify Content
Reduces complexity of text by replacing complex words with simpler alternatives,
shortening sentences, and improving clarity while preserving meaning.
Used in Phase 4 (Quality Assurance) of the textbook project to enhance accessibility.
"""

import argparse
import re
import sys
from typing import List, Dict, Tuple


def simplify_text(text: str) -> str:
    """
    Simplify text by replacing complex words and structures with simpler alternatives.

    Args:
        text: Input text to simplify

    Returns:
        Simplified text
    """
    # Complex to simple word mappings
    complex_to_simple = {
        # Vocabulary simplifications
        r'\butilize\b': 'use',
        r'\butilization\b': 'use',
        r'\butilizing\b': 'using',
        r'\bimplement\b': 'use',
        r'\bimplementation\b': 'use',
        r'\bpotential\b': 'possible',
        r'\bpossibilities\b': 'options',
        r'\butilise\b': 'use',  # British spelling
        r'\butilisation\b': 'use',
        r'\butilising\b': 'using',
        r'\bcommence\b': 'start',
        r'\bterminate\b': 'end',
        r'\bascertain\b': 'find out',
        r'\bdetermine\b': 'find out',
        r'\bidentify\b': 'find',
        r'\bmodify\b': 'change',
        r'\balter\b': 'change',
        r'\bcommence\b': 'start',
        r'\binitiate\b': 'start',
        r'\bconclude\b': 'end',
        r'\bterminate\b': 'end',
        r'\bretrieve\b': 'get',
        r'\bprocure\b': 'get',
        r'\bobtain\b': 'get',
        r'\butilise\b': 'use',
        r'\butilisation\b': 'use',
        r'\butilising\b': 'using',
        r'\bendeavor\b': 'try',
        r'\battempt\b': 'try',
        r'\bpursue\b': 'try',
        r'\bendeavoring\b': 'trying',
        r'\bascertain\b': 'check',
        r'\bverify\b': 'check',
        r'\bconfirm\b': 'check',
        r'\bcommence\b': 'begin',
        r'\binitiate\b': 'begin',
        r'\bcommencing\b': 'beginning',
        r'\binitiating\b': 'beginning',
        r'\bconclude\b': 'finish',
        r'\bterminate\b': 'finish',
        r'\bconcluding\b': 'finishing',
        r'\bterminating\b': 'finishing',
        r'\bretrieve\b': 'find',
        r'\bprocure\b': 'obtain',
        r'\bobtain\b': 'get',
        r'\bprocuring\b': 'obtaining',
        r'\bobtaining\b': 'getting',
        r'\bendeavor\b': 'attempt',
        r'\battempt\b': 'try',
        r'\bpursue\b': 'go after',
        r'\bpursuing\b': 'going after',
        r'\bendeavoring\b': 'attempting',
        r'\bascertain\b': 'determine',
        r'\bverify\b': 'check',
        r'\bconfirm\b': 'check',
        r'\bascertaining\b': 'finding out',
        r'\bverifying\b': 'checking',
        r'\bconfirming\b': 'checking',
        r'\bconsequently\b': 'so',
        r'\btherefore\b': 'so',
        r'\bhence\b': 'so',
        r'\bthus\b': 'so',
        r'\bmoreover\b': 'also',
        r'\bfurthermore\b': 'also',
        r'\badditionally\b': 'also',
        r'\bnevertheless\b': 'but',
        r'\bnonetheless\b': 'but',
        r'\bhowever\b': 'but',
        r'\bnevertheless\b': 'but',
        r'\baccordingly\b': 'so',
        r'\bconsequently\b': 'so',
        r'\bsubsequently\b': 'then',
        r'\bpreviously\b': 'before',
        r'\binitially\b': 'first',
        r'\bultimately\b': 'finally',
        r'\beventually\b': 'finally',
        r'\bfrequently\b': 'often',
        r'\bconstantly\b': 'often',
        r'\boccasionally\b': 'sometimes',
        r'\brarely\b': 'seldom',
        r'\bseldom\b': 'rarely',
        r'\bexceedingly\b': 'very',
        r'\bextremely\b': 'very',
        r'\babsolutely\b': 'very',
        r'\bincredibly\b': 'very',
        r'\btremendously\b': 'very',
        r'\bphenomenally\b': 'very',
        r'\bextraordinarily\b': 'very',
        r'\bexceptionally\b': 'very',
        r'\bparticularly\b': 'especially',
        r'\bespecially\b': 'particularly',
        r'\bnotably\b': 'especially',
        r'\bremarkably\b': 'especially',
        r'\bsurprisingly\b': 'unexpectedly',
        r'\bunexpectedly\b': 'surprisingly',
        r'\binterestingly\b': 'interestingly',
        r'\bamazingly\b': 'surprisingly',
        r'\bstunningly\b': 'surprisingly',
        r'\bimpressively\b': 'remarkably',
        r'\bnoteworthily\b': 'remarkably',
        r'\bunbelievably\b': 'incredibly',
        r'\bunusually\b': 'uncommonly',
        r'\buncommonly\b': 'unusually',
        r'\bparticularly\b': 'especially',
        r'\bexceptionally\b': 'especially',
        r'\bnotably\b': 'especially',
        r'\bremarkably\b': 'especially',
        r'\bexceedingly\b': 'very',
        r'\bextremely\b': 'very',
        r'\babsolutely\b': 'very',
        r'\bincredibly\b': 'very',
        r'\btremendously\b': 'very',
        r'\bphenomenally\b': 'very',
        r'\bextraordinarily\b': 'very',
        r'\bparticularly\b': 'especially',
        r'\bespecially\b': 'particularly',
        r'\bnotably\b': 'especially',
        r'\bremarkably\b': 'especially',
        r'\bconstitute\b': 'form',
        r'\bconstitutes\b': 'forms',
        r'\bconstituted\b': 'formed',
        r'\bconstituting\b': 'forming',
        r'\brequires\b': 'needs',
        r'\brequire\b': 'need',
        r'\brequired\b': 'needed',
        r'\brequiring\b': 'needing',
        r'\bdemonstrate\b': 'show',
        r'\bexhibit\b': 'show',
        r'\bdisplay\b': 'show',
        r'\bpresent\b': 'show',
        r'\billustrate\b': 'show',
        r'\bdemonstrates\b': 'shows',
        r'\bexhibits\b': 'shows',
        r'\bdisplays\b': 'shows',
        r'\bpresents\b': 'shows',
        r'\billustrates\b': 'shows',
        r'\bdemonstrated\b': 'showed',
        r'\bexhibited\b': 'showed',
        r'\bdisplayed\b': 'showed',
        r'\bpresented\b': 'showed',
        r'\billustrated\b': 'showed',
        r'\bdemonstrating\b': 'showing',
        r'\bexhibiting\b': 'showing',
        r'\bdisplaying\b': 'showing',
        r'\bpresenting\b': 'showing',
        r'\billustrating\b': 'showing',
        r'\bcomprise\b': 'include',
        r'\bcomprises\b': 'includes',
        r'\bcomprised\b': 'included',
        r'\bcomprising\b': 'including',
        r'\binvolve\b': 'include',
        r'\binvolves\b': 'includes',
        r'\binvolved\b': 'included',
        r'\binvolving\b': 'including',
        r'\bconstitute\b': 'make up',
        r'\bconstitutes\b': 'makes up',
        r'\bconstituted\b': 'made up',
        r'\bconstituting\b': 'making up',
        r'\bcontains\b': 'has',
        r'\bcontain\b': 'have',
        r'\bcontained\b': 'had',
        r'\bcontaining\b': 'having',
        r'\bpossess\b': 'have',
        r'\bpossesses\b': 'has',
        r'\bpossessed\b': 'had',
        r'\bpossessing\b': 'having',
        r'\badequate\b': 'enough',
        r'\bsufficient\b': 'enough',
        r'\bappropriate\b': 'suitable',
        r'\bsuitable\b': 'appropriate',
        r'\badvisable\b': 'wise',
        r'\bwarranted\b': 'needed',
        r'\bdesirable\b': 'good',
        r'\bpreferable\b': 'better',
        r'\boptimal\b': 'best',
        r'\bideal\b': 'best',
        r'\bperfect\b': 'best',
        r'\bexcellent\b': 'great',
        r'\boutstanding\b': 'great',
        r'\bexceptional\b': 'great',
        r'\bremarkable\b': 'great',
        r'\bextraordinary\b': 'great',
        r'\bphenomenal\b': 'great',
        r'\bmarvelous\b': 'great',
        r'\bwonderful\b': 'great',
        r'\bterrific\b': 'great',
        r'\bfantastic\b': 'great',
        r'\bamazing\b': 'great',
        r'\bstunning\b': 'great',
        r'\bimpressive\b': 'great',
        r'\bnotable\b': 'important',
        r'\bsignificant\b': 'important',
        r'\bimportant\b': 'significant',
        r'\bmeaningful\b': 'important',
        r'\bcrucial\b': 'important',
        r'\bcritical\b': 'important',
        r'\bvital\b': 'important',
        r'\besential\b': 'important',
        r'\bparamount\b': 'important',
        r'\bfundamental\b': 'basic',
        r'\bprimary\b': 'main',
        r'\bprincipal\b': 'main',
        r'\bmain\b': 'primary',
        r'\bchief\b': 'main',
        r'\bcentral\b': 'main',
        r'\bcore\b': 'main',
        r'\besence\b': 'core',
        r'\bheart\b': 'core',
        r'\bnucleus\b': 'core',
        r'\bessence\b': 'core',
        r'\bconsequently\b': 'so',
        r'\btherefore\b': 'so',
        r'\bhence\b': 'so',
        r'\bthus\b': 'so',
        r'\bas a result\b': 'so',
        r'\baccordingly\b': 'so',
        r'\bin order to\b': 'to',
        r'\bfor the purpose of\b': 'to',
        r'\bwith the intention of\b': 'to',
        r'\bin an effort to\b': 'to',
        r'\bwith a view to\b': 'to',
        r'\bas regards\b': 'about',
        r'\bin regard to\b': 'about',
        r'\bwith regard to\b': 'about',
        r'\bwith respect to\b': 'about',
        r'\bin respect to\b': 'about',
        r'\bconcerning\b': 'about',
        r'\bregarding\b': 'about',
        r'\brelating to\b': 'about',
        r'\bin connection with\b': 'about',
        r'\bwith reference to\b': 'about',
        r'\bin the matter of\b': 'about',
        r'\bin the area of\b': 'about',
        r'\bin the field of\b': 'about',
        r'\bin the realm of\b': 'about',
        r'\bin the domain of\b': 'about',
        r'\bin the sphere of\b': 'about',
        r'\bin the context of\b': 'in',
        r'\bwithin the context of\b': 'in',
        r'\bin the framework of\b': 'in',
        r'\bwithin the framework of\b': 'in',
        r'\bin the scope of\b': 'in',
        r'\bwithin the scope of\b': 'in',
        r'\bin the realm of\b': 'in',
        r'\bwithin the realm of\b': 'in',
        r'\bin the sphere of\b': 'in',
        r'\bwithin the sphere of\b': 'in',
        r'\bin the domain of\b': 'in',
        r'\bwithin the domain of\b': 'in',
        r'\bin the area of\b': 'in',
        r'\bwithin the area of\b': 'in',
        r'\bin the field of\b': 'in',
        r'\bwithin the field of\b': 'in',
        r'\bin the sector of\b': 'in',
        r'\bwithin the sector of\b': 'in',
        r'\bin the discipline of\b': 'in',
        r'\bwithin the discipline of\b': 'in',
        r'\bin the branch of\b': 'in',
        r'\bwithin the branch of\b': 'in',
        r'\bin the specialty of\b': 'in',
        r'\bwithin the specialty of\b': 'in',
        r'\bin the aspect of\b': 'in',
        r'\bwithin the aspect of\b': 'in',
        r'\bin the dimension of\b': 'in',
        r'\bwithin the dimension of\b': 'in',
        r'\bin the perspective of\b': 'from',
        r'\bfrom the perspective of\b': 'from',
        r'\bin view of\b': 'because',
        r'\bby virtue of\b': 'because',
        r'\bon account of\b': 'because',
        r'\bin light of\b': 'because',
        r'\bby reason of\b': 'because',
        r'\bin consequence of\b': 'because',
        r'\binasmuch as\b': 'because',
        r'\bin that\b': 'because',
        r'\bsince\b': 'because',
        r'\bas\b': 'because',
        r'\bwhereas\b': 'but',
        r'\bwhile\b': 'but',
        r'\balthough\b': 'but',
        r'\bthough\b': 'but',
        r'\beven though\b': 'but',
        r'\bin contrast to\b': 'but',
        r'\bcontrary to\b': 'but',
        r'\bin opposition to\b': 'but',
        r'\bin juxtaposition to\b': 'but',
        r'\bin parallel to\b': 'and',
        r'\balongside\b': 'with',
        r'\bin conjunction with\b': 'with',
        r'\btogether with\b': 'with',
        r'\balong with\b': 'with',
        r'\bin unison with\b': 'with',
        r'\bin harmony with\b': 'with',
        r'\bin concert with\b': 'with',
        r'\bin collaboration with\b': 'with',
        r'\bin cooperation with\b': 'with',
        r'\bin partnership with\b': 'with',
        r'\bin association with\b': 'with',
        r'\bin connection with\b': 'with',
        r'\bin relation to\b': 'with',
        r'\bin comparison to\b': 'with',
        r'\bcompared to\b': 'like',
        r'\bcompared with\b': 'like',
        r'\bin comparison with\b': 'like',
        r'\bsimilar to\b': 'like',
        r'\bakin to\b': 'like',
        r'\bresembling\b': 'like',
        r'\bidentical to\b': 'like',
        r'\bequivalent to\b': 'like',
        r'\bcorresponding to\b': 'like',
        r'\banalogous to\b': 'like',
        r'\bcomparable to\b': 'like',
        r'\bsimilar\b': 'like',
        r'\bidentical\b': 'same',
        r'\bequivalent\b': 'same',
        r'\bcorresponding\b': 'same',
        r'\banalogous\b': 'similar',
        r'\bcomparable\b': 'similar',
        r'\bsimilarly\b': 'likewise',
        r'\bin the same way\b': 'likewise',
        r'\balso\b': 'too',
        r'\bas well\b': 'too',
        r'\bin addition\b': 'also',
        r'\bfurthermore\b': 'also',
        r'\bmoreover\b': 'also',
        r'\badditionally\b': 'also',
        r'\bwhat is more\b': 'also',
        r'\bnot only\b': 'not just',
        r'\bnot only that\b': 'also',
        r'\bapart from\b': 'besides',
        r'\bin addition to\b': 'besides',
        r'\balong with\b': 'besides',
        r'\btogether with\b': 'with',
        r'\bin unison with\b': 'with',
        r'\balongside\b': 'with',
        r'\bin conjunction with\b': 'with',
        r'\bin collaboration with\b': 'with',
        r'\bin cooperation with\b': 'with',
        r'\bin partnership with\b': 'with',
        r'\bin association with\b': 'with',
        r'\blikewise\b': 'also',
        r'\bin the same way\b': 'likewise',
        r'\bin like manner\b': 'likewise',
        r'\bin similar fashion\b': 'likewise',
        r'\bin the same fashion\b': 'likewise',
        r'\bin similar manner\b': 'likewise',
        r'\bin like fashion\b': 'likewise',
        r'\bin like manner\b': 'likewise',
        r'\bin similar terms\b': 'likewise',
        r'\bin the same terms\b': 'likewise',
        r'\bin like terms\b': 'likewise',
        r'\bin similar way\b': 'likewise',
        r'\bin the same way\b': 'likewise',
        r'\bin like way\b': 'likewise',
        r'\bin a similar way\b': 'likewise',
        r'\bin a like way\b': 'likewise',
        r'\bin a like fashion\b': 'likewise',
        r'\bin a similar fashion\b': 'likewise',
        r'\bin a like manner\b': 'likewise',
        r'\bin a similar manner\b': 'likewise',
        r'\bin a similar way\b': 'likewise',
        r'\bin a like way\b': 'likewise',
        r'\bin the same way as\b': 'like',
        r'\bin a similar way to\b': 'like',
        r'\bin a like way to\b': 'like',
        r'\bin contrast\b': 'but',
        r'\bin opposition\b': 'but',
        r'\bin contrast to\b': 'but',
        r'\bin opposition to\b': 'but',
        r'\bin juxtaposition to\b': 'but',
        r'\bin parallel to\b': 'and',
    }

    # Apply word simplifications
    simplified = text
    for complex_word, simple_word in complex_to_simple.items():
        simplified = re.sub(complex_word, simple_word, simplified, flags=re.IGNORECASE)

    # Simplify long sentences (split sentences longer than 25 words)
    simplified = _simplify_long_sentences(simplified)

    return simplified


def _simplify_long_sentences(text: str) -> str:
    """
    Break down long sentences into shorter ones for better readability.
    """
    sentences = re.split(r'([.!?]+)', text)
    simplified_sentences = []

    for i in range(0, len(sentences), 2):
        sentence = sentences[i]
        punctuation = sentences[i+1] if i+1 < len(sentences) else ''

        # Split long sentences based on conjunctions
        words = sentence.split()
        if len(words) > 25:
            # Look for natural breaking points (conjunctions)
            simplified_sentences.extend(_break_long_sentence(sentence))
        else:
            simplified_sentences.append(sentence + punctuation)

    return ' '.join(simplified_sentences)


def _break_long_sentence(sentence: str) -> List[str]:
    """
    Break a long sentence into smaller parts.
    """
    # Find conjunctions or semicolons that can be used as breaking points
    conjunctions = [' and ', ' or ', ' but ', ' so ', ' yet ', ' for ', ' nor ']

    for conj in conjunctions:
        parts = sentence.split(conj)
        if len(parts) > 1:
            result = []
            for i, part in enumerate(parts):
                if i == 0:
                    result.append(part.strip() + '.')
                else:
                    # Capitalize first letter of subsequent parts
                    part = part.strip()
                    if part:
                        if part[0].islower():
                            part = part[0].upper() + part[1:]
                        result.append('Also, ' + part + '.')
            return result

    # If no conjunctions found, just split in half
    words = sentence.split()
    mid = len(words) // 2
    if mid > 0:
        first_half = ' '.join(words[:mid])
        second_half = ' '.join(words[mid:])
        return [first_half + '.', second_half + '.']

    return [sentence]


def main():
    parser = argparse.ArgumentParser(description='Simplify text content for better readability')
    parser.add_argument('input_file', help='Input text file to simplify')
    parser.add_argument('-o', '--output', help='Output file for simplified text (default: stdout)')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            text = f.read()

        simplified_text = simplify_text(text)

        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(simplified_text)
            print(f"Simplified text written to {args.output}")
        else:
            print(simplified_text)

    except FileNotFoundError as e:
        print(f"Error: File not found - {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()