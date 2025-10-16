"""
main.py
--------
Phase 3 + 3.5 Testing:
- GAIA-0 can now save memories and reflect upon them.
- This marks the beginning of persistent cognition and self-reflection.
"""

from core.memory import MemorySystem
from core.brain import Brain

def main():
    """
    Main testing routine for GAIA Phase 3 and 3.5.
    Allows the user to record new memories and ask GAIA to reflect on them
    """
    
    # Initialize GAIA's memory system
    memory = MemorySystem()
    
    # Initialize the reflection/brain module
    brain = Brain(memory)
    
    print("=== GAIA :: MEMORY & REFLECTION TEST ===")
    print("Type 'reflect' to see GAIA's daily thoughts.")
    print("Type 'recent' to see recent memories.")
    print("Type 'exit' to quit.\n")
    
    # Continuous Loop to interact with GAIA's memory
    while True:
        # Ask the user for input
        user_input = input("Enter something GAIA learned today: ").strip()
        
        # Exit condition
        if user_input.lower() == "exit":
            print("Goodbye.")
            break
        
        # Trigger reflection summary
        elif user_input.lower() == "reflect":
            print("\n--- REFLECTION ---")
            print(brain.reflect_today())
            print("------------------\n")
            
        # Show recent memory log
        elif user_input.lower() == "recent":
            print("\n--- RECENT MEMORIES ---")
            print(brain.summarize_recent())
            print("-----------------------\n")
            
        # Otherwise, treat input as a new memory entry
        else:
            memory.add_memory(user_input, tags=["learning", "reflection"])
            print("Memory saved successfully!\n")
            
if __name__ == "__main__":
    main()