"""
generator.py
-------------
Phase 2: Sentence generation from GAIA's internal lexicon.

This module enables GAIA to build simple Subject-Verb-Object (SVO) sentences
by randomly combining known nouns and verbs from the dictionary.

Later phases will expand this with grammar rules, adjectives, and articles.
"""

import random
from core.parser import Lexicon

class SentenceGenerator:
    def __init__(self, lexicon: Lexicon):
        """
        Initialize the SentenceGenerator with access to GAIA's Lexicon.
        
        args:
            lexicon (Lexicon): The loaded Lexicon instance that holds all word data.
        """
        self.lexicon = lexicon
    
    def get_words_by_type(self, word_type: str) -> list:
        """
        Retrieve all words from the lexicon that match a specific part of speech.
        
        args:
            word_type (str): The word type to filter by (e.g. "noun", "verb").
            
        Returns:
            list: A list of all words that match the given type.
        """
        return [
            word for word, info in self.lexicon.data.items()
            if info.get("type") == word_type
        ]
    
    def generate_sentence(self) -> str:
        """
        Generate a simple SVO sentence using random words from the lexicon.
        
        Returns:
            str: A simple generated sentence (e.g. "Katze läuft Maus").
        """
        nouns = self.get_words_by_type("noun")
        verbs = self.get_words_by_type("verb")
        
        # Safety check: ensure there are enough words to form a sentence
        if len(nouns) < 2 or not verbs:
            return "Error: Not enough words in dictionary to form a sentence."
        
        # Randomly choose subject, verb, and object
        subject = random.choice(nouns)
        verb =  random.choice(verbs)
        obj = random.choice([n for n in nouns if n != subject]) # avoid same noun twice
        
        # Build and return the sentence
        return f"{subject.capitalize()} {verb} {obj}"


