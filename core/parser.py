"""
parser.py
-----------
Loads GAIA's lexical data and provides access to word information.

This is the core of Phase 1: word understanding.

Each word is stored in a JSON file with:
    - part_of_speech: word type (noun,verb etc.)
    - definitions: list of meanings
    - examples: example sentences
"""

# Import the JSON module to read JSON files
import json
# Import Path from pathlib to handle file paths across different platforms
from pathlib import Path

class Lexicon:
    """
    Lexicon class manages GAIA's dictionary.
    It can load the dictionary, retrieve word information,
    and list all known words.
    """
    def __init__(self, dictionary_path: str):
        """
        Constructor: initializes the Lexicon instance
        
        Steps:
            1. Converts the input string path to a Path object (Platform-independent)
            2. Loads the dictionary into self.data
        
        :param dictionary.path: Path to the JSON file containing lexical data.
        """
        # Store the path to the JSON dictionary
        self.dictionary_path = Path(dictionary_path)
        # Load the dictionary data into memory as a Python dictionary
        self.data = self.load_dictionary()
        
    def load_dictionary(self) -> dict:
        """
        Loads the JSON dictionary into memory.

        Steps:
        1. Check if the file exists, otherwise raise an error
        2. Open the file in read mode with UTF-8 encoding
        3. Convert JSON content into a Python dictionary
        4. Return the dictionary

        :return: Dictionary containing all words and their properties
        """
        # Check if the file exists
        if not self.dictionary_path.exists():
            # Raise an error if the file is not found
            raise FileNotFoundError(f"Dictionary not found at {self.dictionary_path}")
            
        # Open the JSON file in read mode "r" with UTF-8 encoding
        with open(self.dictionary_path, "r", encoding="utf-8") as file:
            # Load JSON content into a Python dictionary and return it
            return json.load(file)
        
    def get_word_info(self, word: str) -> dict:
        """
        Retrieves all information about a given word.

        Steps:
        1. Converts the input word to lowercase (case-insensitive search)
        2. Checks if the word exists in the dictionary
        3. Returns the word data or None if unknown

        :param word: Word to look up in the lexicon
        :return: Dictionary with part_of_speech, definitions, examples or None
        """
        # First try lowercase
        result = self.data.get(word.lower())
        if result:
            return result
        
        # Use dictionary's get() method to fetch the word info
        return self.data.get(word, None)
    
    def list_all_words(self) -> list:
        """
        Returns a list of all known words in the lexicon.

        Steps:
        1. Retrieve all dictionary keys (all words)
        2. Return them as a list

        :return: List of all words as strings
        """
        return list(self.data.keys())
    
