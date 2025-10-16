"""
generator.py
-------------
Phase 2.5: Targeted sentence generation and basic syntax logic.

This module allows GAIA-0 to form sentences intentionally using specific subjects or verbs.
It extends random sentence generation by introducing guided generation methods.
"""

import random
from core.parser import Lexicon

class SentenceGenerator:
    def __init__(self, lexicon: Lexicon):
        """
        Initialize the SentenceGenerator with access to GAIA's Lexicon.
        The Lexicon provides word type information (noun, verb, etc.).
        """
        self.lexicon = lexicon
    
    def get_words_by_type(self, word_type: str) -> list:
        """
        Return a list of all words in the dictionary that match a given type.
        Example: get_words_by_type("noun") → ["katze", "hund", "maus"]
        """
        return [
            word for word, info in self.lexicon.data.items()
            if info.get("type") == word_type
        ]
    
    def generate_sentence(self) -> str:
        """
        Generate a random sentence in simple Subject–Verb–Object form.
        Requires at least two nouns and one verb in the Lexicon.
        """
        nouns = self.get_words_by_type("noun")
        verbs = self.get_words_by_type("verb")
        
        # Basic word count check to prevent runtime errors
        if len(nouns) < 2 or not verbs:
            return "Error: Not enough words in dictionary to form a sentence."
        
        # Randomly choose subject, verb, and object
        subject = random.choice(nouns)
        verb =  random.choice(verbs)
        obj = random.choice([n for n in nouns if n != subject]) # avoid same noun twice
        
        # Return capitalized sentence
        return f"{subject.capitalize()} {verb} {obj}"
    
    # Phase 2.5 new function
    def generate_with_subject(self, subject: str) -> str:
        """
        Generate a sentence that starts with the given subject (noun).
        If the subject is unknown or not a noun, an error message is returned.
        """
        subject = subject.lower()
        info = self.lexicon.get_word_info(subject)
        
        # Validate if the subject exists and is a noun
        if not info or info.get("type") != "noun":
            return f"Error: '{subject}' is not a known noun."
        
        # Collect possible verbs and nouns for the object
        verbs = self.get_words_by_type("verb")
        nouns = [n for n in self.get_words_by_type("noun") if n != subject]
        
        if not verbs or not nouns:
            return "Error: Not enough words to form a sentence."
        
        # Randomly select elements for the sentence
        verb = random.choice(verbs)
        obj = random.choice(nouns)
        
        return f"{subject.capitalize()} {verb} {obj}"
    
    def generate_with_verb(self, verb: str) -> str:
        """
        Generate a sentence that includes the given verb.
        If the verb is unknown or not a verb, an error message is returned.
        """
        verb = verb.lower()
        info = self.lexicon.get_word_info(verb)
        
        # Validate if the verb exists and is correctly categorized
        if not info or info.get("type") != "verb":
            return f"Error: '{verb}' is not a known verb."
        
        nouns = self.get_words_by_type("noun")
        
        if len(nouns) < 2:
            return "Error: Not enough nouns to form a sentence"
        
        # Choose subject and object dynamically
        subject = random.choice(nouns)
        obj = random.choice([n for n in nouns if n != subject])
        
        return f"{subject.capitalize()} {verb} {obj}"
