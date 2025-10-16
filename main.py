"""
main.py
--------
Phase 4 Testing: Autonomous Reasoning

- GAIA-0 can now store facts, apply rules, and suggest consequences.
- Interactive testing of logic system integrated with memory and reflection.
"""
from core.memory import MemorySystem
from core.brain import Brain
from core.logic import LogicSystem

def main():
    """
    Main interactive routine for Phase 4.

    Users can:
    - Add new facts
    - Ask GAIA to reflect on memories
    - Ask GAIA to infer logical consequences based on stored facts
    """
    
    # Instantiate GAIA's memory system
    memory = MemorySystem()
    
    # Instantiate GAIA's reflection system (Phase 3.5)
    brain = Brain(memory)
    
    # Instantiate GAIA's logic/reasoning system (Phase 4)
    logic = LogicSystem(memory)
    
    print("=== GAIA-0 :: PHASE 4 AUTONOMOUS REASONING ===")
    print("Type 'reflect' to see reflections, 'logic' to see inferences, 'exit' to quit.\n")
    
    # Continuous Loop to interact with GAIA's memory
    while True:
        # Ask user to input a fact or command
        user_input = input("Enter new Fact for GAIA: ").strip()
        
        # Exit the loop and program
        if user_input.lower() == "exit":
            print("Goodbye.")
            break
        
        # Trigger GAIA's reflection summary (Phase 3.5)
        elif user_input.lower() == "reflect":
            print("\n--- REFLECTION ---")
            print(brain.reflect_today())            # Reflect on today's memories
            print(brain.summarize_recent())         # Summarize recent memories
            print("------------------\n")
            
        # Trigger GAIA's logic system to evaluate rules
        elif user_input.lower() == "logic":
            inferences = logic.infer_all()
            print("\n--- LOGICAL INFERENCES ---")
            
            
            if not inferences:
                print("No inferences available")
            else:
                # Loop over facts and their inferred consequences
                for fact, consequences in inferences.items():
                    print(f"Fact: {fact}")
                    for c in consequences:
                        print(f" -> Suggestion: {c}")
            print("---------------------------\n")
            
        # Treat any other input as a new fact to store in memory
        else:
            memory.add_memory(user_input, tags=["fact"])
            print("Fact stored successfully!\n")
            
if __name__ == "__main__":
    main()