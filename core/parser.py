"""
parser.py
---------
GAIA-0 Phase 4.5 Lexicon + POS Detection

Responsibilities:
- Load multiple lexical sources:
    - structured dictionary.json
    - large external wordlist (dwyl format)
    - learned_words.json (GAIA's personal POS store)
- Provide methods for:
    - Tokenizing sentences
    - Detecting POS for each token using lexicon + heuristics
"""

import json
from pathlib import Path
from typing import List, Optional, Dict, Any

class Lexicon:
    def __init__(self,
                 dictionary_path="data/knowledge/dictionary.json",
                 external_wordlist_path="data/knowledge/words_dictionary.json",
                 pos_rules_path="data/knowledge/pos_rules.json",
                 syntax_patterns_path="data/knowledge/syntax_patterns.json",
                 learned_words_path="data/knowledge/learned_words.json"):
        """
        Initialize Lexicon and load all JSON resources
        """
        self.dictionary_path = Path(dictionary_path)
        self.external_wordlist_path = Path(external_wordlist_path)
        self.pos_rules_path = Path(pos_rules_path)
        self.syntax_patterns_path = Path(syntax_patterns_path)
        self.learned_words_path = Path(learned_words_path)

        self.data: Dict[str, Any] = {}            # structured dictionary
        self.external_words: Dict[str, Any] = {}  # external wordlist
        self.pos_rules: Dict[str, Any] = {}       # POS heuristics
        self.syntax_patterns: Dict[str, Any] = {} # sentence patterns
        self.learned_words: Dict[str, Any] = {}   # GAIA's learned POS

        self.load_all_resources()

    def load_all_resources(self):
        """
        Load all JSON resources, missing files handled gracefully
        """
        self.data = self._load_json_safely(self.dictionary_path) or {}
        self.external_words = self._load_json_safely(self.external_wordlist_path) or {}
        self.pos_rules = self._load_json_safely(self.pos_rules_path) or {}
        self.syntax_patterns = self._load_json_safely(self.syntax_patterns_path) or {}
        self.learned_words = self._load_json_safely(self.learned_words_path) or {}

    def _load_json_safely(self, path) -> Optional[dict]:
        """Allow both str and Path objects."""
        path = Path(path)  # <-- konvertiere sicher
        if not path.exists():
            print(f"[Lexicon] Warning: JSON file not found: {path}")
            return None
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[Lexicon] Error loading JSON {path}: {e}")
            return None

    def save_learned_words(self):
        """Save GAIA's learned words"""
        try:
            self.learned_words_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.learned_words_path, "w", encoding="utf-8") as f:
                json.dump(self.learned_words, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[Lexicon] Error saving learned words: {e}")
            
    def learn_word(self, word: str, pos: str, confidence: float = 0.8):
        """
        Store a learned POS for a word in learned_words.json.
        If the word exists already, update confidence by averaging.
        """
        key = word.lower()
        existing = self.learned_words.get(key)
        if existing:
            existing_conf = existing.get("confidence", 0.5)
            new_conf = (existing_conf + confidence) / 2
            existing["confidence"] = new_conf
            existing["type"] = pos
        else:
            self.learned_words[key] = {"type": pos, "confidence": confidence}
    
        # Persist to disk
        self.save_learned_words()

    # ----------------------------
    # Sentence parsing & POS
    # ----------------------------
    def parse_sentence(self, sentence: str) -> List[str]:
        """Tokenize a sentence (simple space-split)"""
        return sentence.strip().split()

    def get_word_pos(self, word: str, context_tokens: Optional[List[str]] = None, index: Optional[int] = None) -> Optional[Dict[str, Any]]:
        """
        Determine POS for a word using:
        learned_words -> dictionary -> pos_rules -> context heuristics -> external wordlist
        """
        key = word.lower()

        # 1) learned words
        if key in self.learned_words:
            info = dict(self.learned_words[key])
            info["type"] = info.get("type", info.get("part_of_speech", "unknown"))
            return info

        # 2) structured dictionary
        if key in self.data:
            entry = dict(self.data[key])
            entry["type"] = entry.get("type") or entry.get("part_of_speech") or "unknown"
            return {"type": entry["type"], "confidence": 0.95, "source": "dictionary"}

        # 3) heuristic POS
        heuristic = self.detect_pos_via_rules(key)
        if heuristic:
            return {"type": heuristic, "confidence": 0.6, "source": "heuristic"}

        # 4) external wordlist fallback
        if key in self.external_words:
            return {"type": "unknown", "confidence": 0.3, "exists": True, "source": "external_wordlist"}

        # completely unknown
        return {"type": "unknown", "confidence": 0.0}

    def detect_pos_via_rules(self, word: str) -> Optional[str]:
        """Detect POS using pos_rules.json heuristics"""
        w = word.lower()
        for pos_name, cfg in self.pos_rules.items():
            # check word lists
            for wlist_word in cfg.get("words", []):
                if w == wlist_word.lower():
                    return pos_name
            # check suffixes
            for suffix in cfg.get("suffixes", []):
                if w.endswith(suffix.lower()):
                    return pos_name
            # check prefixes
            for prefix in cfg.get("prefixes", []):
                if w.startswith(prefix.lower()):
                    return pos_name
        return None