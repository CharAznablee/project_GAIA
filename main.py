"""
main.py
--------
Phase 1.5: Sentence parsing and SVO (Subject-Verb-Object) analysis

- GAIA-0 analyzes simple sentences to identify Subject, Verb, and Object
- Includes predefined test sentences for automatic demonstration
- Also allows interactive sentence input
- Warns if words are not found in the dictionary
"""

# Import the Lexicon class from core/parser.py
from core.parser import Lexicon

# Import the grammar class from core/grammar.py
from core.grammar import Grammar

# Initialize the Lexicon with the path to dictionary.json
lexicon = Lexicon("data/knowledge/dictionary.json")

# Initialize Grammar with the Lexicon instance
grammar = Grammar(lexicon)

# ---- Predefined test sentences for Phase 1.5 ----
test_sentences = [
    "Katze laufen Maus",
    "Hund fressen Wurst",
    "Vogel fliegen Baum"
]

print("\n--- Test Sentences ---")
for s in test_sentences:
    # Parse the sentence using Grammar
    analysis = grammar.parse_sentence(s)
    # Display the analysis result
    print(f"Sentence: '{s}' -> {analysis}")
print("--- End of tests ---\n")

# --- Interactive Loop for user input ---
while True:
    # Ask the user for a sentence
    sentence = input("Enter a sentence for GAIA to analyze (or 'exit' to quit): ").strip()
    
    # Exit condition
    if sentence.lower() == "exit":
        break
    
    # --- Small error handling: warn about unknown words ---
    for token in sentence.strip().split():
        info = lexicon.get_word_info(token.lower())
        if not info:
            print(f"Warning: '{token}' not found in dictionary")
            continue
    
    # Parse the sentence to identify Subject, Verb, Object
    analysis = grammar.parse_sentence(sentence)
    
    # Display results
    print("\nGAIA Sentence Analysis:")
    print(f"Subject: {analysis['subject']}")
    print(f"Verb: {analysis['verb']}")
    print(f"Object: {analysis['object']}")
