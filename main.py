"""
main.py
--------
Phase 4.5 – External Dictionary Integration + POS & Syntax Testing

GAIA-0 now uses external JSON dictionaries to:
- Identify words (from a large JSON dictionary file)
- Detect parts of speech (using pos_rules.json)
- Validate simple sentence structures (using syntax_patterns.json)
- Retrieve grammar hints (using grammar_rules.json)

This marks GAIA’s transition from raw word recognition (Phase 1–3)
to structured grammatical understanding.
"""

import json
from core.parser import Lexicon
from core.grammar import GrammarSystem


def main():
    """
    Interactive test for Phase 4.5.
    Allows the user to enter sentences and see how GAIA parses and classifies them.
    """

    print("=== GAIA :: PHASE 4.5 TEST ===")
    print("GAIA now uses external dictionaries for grammar and syntax.")
    print("Type a sentence to analyze, or 'exit' to quit.\n")

    # Initialize core systems
    parser = Lexicon()
    grammar = GrammarSystem()

    while True:
        user_input = input("Enter a sentence: ").strip()

        if user_input.lower() == "exit":
            print("Exiting GAIA test environment. Goodbye.")
            break

        # --- 1️ PARSE SENTENCE ---
        tokens = parser.parse_sentence(user_input)
        print("\n[1] Tokenized Sentence:")
        print(tokens)

        # --- 2️ POS DETECTION ---
        print("\n[2] Detected Parts of Speech:")
        pos_tokens = []
        for word in tokens:
            pos = grammar.get_pos(word)
            pos_tokens.append((word, pos))
            print(f"  {word:<15} → {pos}")

        # --- 3️ SYNTAX VALIDATION ---
        print("\n[3] Syntax Validation:")
        grammar.validate_syntax(pos_tokens)

        # --- 4️ GRAMMAR HINTS ---
        print("\n[4] Grammar Hints:")
        for word in tokens:
            hint = grammar.get_grammar_hint(word)
            print(f"  {word:<15} → {hint}")

        print("\n-----------------------------------------\n")
        
        for index, word in enumerate(tokens):
            pos_info = parser.get_word_pos(word, context_tokens=tokens, index=index)
            pos_type = pos_info["type"]
            
            # Speichern in learned_words.json
            parser.learn_word(word, pos_type, confidence=pos_info.get("confidence", 0.8))
            
            pos_tokens.append((word, pos_type))


if __name__ == "__main__":
    main()