"""
main.py
--------
Phase 2: Simple sentence generation using GAIA-0's Lexicon.

In this phase, GAIA-0 can generate random Subject-Verb-Object (SVO) sentences
based on the known words in dictionary.json.

- Option 1: Generate random sentences automatically
- Option 2: Let the user trigger generation interactively
"""
# Import the Lexicon class from core/parser.py
from core.parser import Lexicon

# Import the grammar class from core/grammar.py
from core.grammar import Grammar

# Import the SentenceGenerator class from core/generator.py
from core.generator import SentenceGenerator

# Initialize the Lexicon with the path to dictionary.json
lexicon = Lexicon("data/knowledge/dictionary.json")

# Initialize Grammar with the Lexicon instance
grammar = Grammar(lexicon)

# Initialize the SentenceGenerator for Phase 2
generator = SentenceGenerator(lexicon)

print("\n--- Phase 2: Sentence Generation Test ---")

# --- Option 1: Generate predefined number of random sentences ---
for i in range(5):
    sentence = generator.generate_sentence()
    print(f"Generated Sentence {i+1}: {sentence}")
    
print("--- End of automatic generation ---\n")

# --- Option 2: Interactive user Loop ---
while True:
    user_input = input("Type 'generate' for a new sentence or 'exit' to quit: ").strip().lower()
    
    if user_input == "exit":
        print("Exiting GAIA Sentence Generator.")
        break
    elif user_input == "generate":
        # Generate a new random sentence
        sentence = generator.generate_sentence()
        print(f"GAIA says: {sentence}")
    else:
        print("Invalid command. Please type 'generate' or 'exit'.")
