"""
grammar.py
----------
GAIA-0 Phase 4.5 Grammar System

Responsibilities:
- Validate sentence structures based on syntax_patterns.json
- Provide grammar hints from grammar_rules.json
- Integrate with Lexicon for POS info
- Support flexible endings (optional adjectives/adverbs)
"""

from core.parser import Lexicon

class GrammarSystem:
    def __init__(self):
        self.lexicon = Lexicon()
        # Load grammar rules (for hints)
        self.grammar_rules = self.lexicon._load_json_safely(
            "data/knowledge/grammar_rules.json"
        ).get("rules", {})
        # Load syntax patterns
        self.syntax_patterns = self.lexicon.syntax_patterns.get("patterns", [])

    def get_pos(self, word, tokens=None, index=None):
        """Return the POS type of a word using Lexicon"""
        info = self.lexicon.get_word_pos(word, context_tokens=tokens, index=index)
        if info:
            return info.get("type", "unknown")
        return "unknown"

    def validate_syntax(self, pos_tokens):
        """
        pos_tokens: list of tuples (word, pos)
        Compare POS sequence against known syntax patterns
        Supports flexible endings (extra adjectives/adverbs at the end)
        """
        pos_sequence = [p for _, p in pos_tokens]
        matched = False

        for pattern in self.syntax_patterns:
            pattern_seq = pattern["sequence"]
            # Check if pos_sequence starts with pattern_seq
            if pos_sequence[:len(pattern_seq)] == pattern_seq:
                print(f"[INFO] Syntax pattern matched: {pattern['name']}")
                matched = True

        if not matched:
            print("[INFO] No syntax pattern matched.")

    def get_grammar_hint(self, word):
        """
        Return a human-readable grammar hint for a word
        """
        # Normalize word to lower for dictionary lookup
        key = word.lower()
        # Check exact matches first
        if key in self.grammar_rules:
            return self.grammar_rules[key]
        # Otherwise, check by POS
        pos_info = self.lexicon.get_word_pos(word)
        if pos_info:
            pos_type = pos_info.get("type")
            return self.grammar_rules.get(pos_type, "No specific grammar rule found.")
        return "No specific grammar rule found."