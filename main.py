"""
main.py
--------
Phase 2.5: Targeted sentence generation test.
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

print("\n--- Phase 2.5: Targeted Sentence Generation ---")

while True:
    print("\nOptions:")
    print("1 - Generate random sentence")
    print("2 - Generate sentence with specific subject")
    print("3 - Generate sentence with specific verb")
    print("exit - Quit program")
    
    user_input = input("\nSelect an option: ").strip().lower()
    
    if user_input == "exit":
        print("Exiting GAIA Sentence Generator.")
        break
    elif user_input == "1":
        print("GAIA says:", generator.generate_sentence())
    elif user_input == "2":
        subject = input("Enter a subject (noun): ").strip()
        print("GAIA says:", generator.generate_with_subject(subject))
    elif user_input == "3":
        verb = input("Enter a verb: ").strip()
        print("GAIA says:", generator.generate_with_verb(verb))
    else:
        print("Invalid option. Please choose 1, 2, 3, or exit.")
