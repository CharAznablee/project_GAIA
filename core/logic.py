"""
logic.py
--------
Phase 4: Autonomous Reasoning

This module allows GAIA-0 to make simple logical inferences based on stored facts.
It uses rules from rules.json and evaluates them against GAIA's memory system.
"""

import json
from pathlib import Path

class LogicSystem:
    def __init__(self, memory, rules_path="data/knowledge/rules.json"):
        """
        Initialize the logic system.
        :param memory: MemorySystem instance for GAIA's known facts
        :param rules_path: path to JSON file containing if-then rules
        """
        self.memory = memory # Access GAIA's memory
        self.rules_path = Path(rules_path)
        self.rules = self.load_rules() # Load rules at initialization
        
    def load_rules(self):
        """
        Load logical rules from a JSON file.

        Returns a list of dicts: [{"condition": "...", "consequence": "..."}]

        If the file does not exist, returns an empty list and prints a warning.
        """
        if not self.rules_path.exists():
            print(f"Warning: rules.json not found at {self.rules_path}")
            return []
        
        with open(self.rules_path, "r", encoding="utf-8") as f:
            return json.load(f)
        
    def evaluate(self, fact):
        """
        Evaluate a single fact against all loaded rules.

        :param fact: str, a fact stored in GAIA's memory
        :return: list of consequences (strings) triggered by this fact
        """
        consequences = []
        
        # Loop through each rule to check if the condition matches the fact
        for rule in self.rules:
            # Case-insensitive exact match
            if rule["condition"].lower() == fact.lower():
                consequences.append(rule["consequence"])
                
        return consequences
    
    def infer_all(self):
        """
        Apply all rules to all stored memories/facts.

        Returns a dictionary mapping each fact to its inferred consequences.
        """
        results = {}
        
        # Iterate over all memory entries
        for mem in self.memory.data["memories"]:
            fact = mem["content"]
            consequences = self.evaluate(fact)
            
            if consequences: # Only store facts with matching rules
                results[fact] = consequences
                
        return results