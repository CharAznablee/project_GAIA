"""
main.py
--------
Entry point for Phase 1: testing GAIA-0's basic word understanding.

This script demonstrates how to:
- Load the Lexicon
- Retrieve information about words
- Display part of speech, definitions, and example sentences
"""

# Import the Lexicon class from core/parser.py
from core.parser import Lexicon

# Initialize the Lexicon with the path to dictionary.json
lexicon = Lexicon("data/knowledge/dictionary.json")

# Start an infinite Loop to query multiple words
while True:
    # Ask the user to input a word
    word = input("Enter a word for GAIA to analyze (or 'exit' to quit): ").strip()
    
    # Check if the user wants to exit the programm
    if word.lower() == "exit":
        break # Exit the loop and end the programm
    
    # Retrieve word information from the Lexicon
    info = lexicon.get_word_info(word)
    
    # If the word exists in the dictionary
    if info:
        print(f"\nWord: {word}")
        print(f"Part of speech: {info['part_of_speech']}")
        print("Definitions:")
        # Loop through all definitions and print them
        for definition in info["definitions"]:
            print(f" - {definition}")
        print("Example sentences:")
        # Loop through all example sentences and print them
        for example in info["examples"]:
            print(f" - {example}")
    else:
        # If the word is unknown to GAIA
        print(f"\nGAIA does not yet know the word '{word}'.")