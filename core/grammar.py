"""
grammar.py
----------
Handles basic sentence structure analysis for GAIA-0.

Phase 1.5: Identify simple sentence components (Subject, Verb, Object)
"""

from core.parser import Lexicon

class Grammar:
    """
    Grammar class analyzes simple sentence structures using a given Lexicon.
    """
    def __init__(self, lexicon: Lexicon):
        """
        Constructor: receives an instance of Lexicon to access word information.
        """
        # Store the reference to Lexicon instance to query word info
        self.lexicon = lexicon
        
    def parse_sentence(self, sentence: str) -> dict:
        """
        Parse a simple sentence and try to identify Subject, Verb, and Object.

        Steps:
        1. Split the sentence into words (tokens)
        2. Identify the part of speech of each word
        3. Assign the first noun as Subject
        4. Assign the first verb as Verb
        5. Assign the next noun as Object (if exists)

        :param sentence: Input sentence as a string
        :return: Dictionary with 'subject', 'verb', 'object' keys
        """
        # Split the sentece into a list of words
        tokens =  sentence.strip().lower().split()
        # Initialize variables to store identified components
        subject = None
        verb = None
        obj = None
        
        # Loop through each word token in sentence
        for token in tokens:
            # Get word information from Lexicon
            info = self.lexicon.get_word_info(token)
            # Skip the token if it is unknown in the dictionary
            if not info:
                continue # Skip unknown words
            
            # Retrieve the part of speech (POS) of the current word
            pos = info['part_of_speech']
            
            # Assign the first noun found as Subject
            if pos == 'noun' and subject is None:
                subject = token
            # Assign the first verb found as verb
            elif pos == 'verb' and verb is None:
                verb = token
            # Assign the next noun after Subject and Verb as Object
            elif pos == 'noun' and subject is not None and verb is not None and obj is None:
                obj = token
        
        # Return the analysis as a dictionary
        return {
            'subject': subject,
            'verb': verb,
            'object': obj
        }
        