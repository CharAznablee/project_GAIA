"""
memory.py
----------
Phase 3: Basic Memory System

This module allows GAIA to store, retrieve, and manage its own memories.
Each memory represents a reflection, event, or learned concept.
"""

import json
from datetime import datetime
from pathlib import Path

class MemorySystem:
    def __init__(self, memory_path: str = "data/knowledge/memories.json"):
        """
        Initialize the memory system and ensure the memory file exists.
        """
        self.memory_path = Path(memory_path)
        self.data = self.load_memories()
        
    def load_memories(self) -> dict:
        """
        Load memory data from the JSON file.
        If the file does not exist, return an empty memory structure.
        """
        if not self.memory_path.exists():
            return {"memories": []}
        with open(self.memory_path, "r", encoding="utf-8") as f:
            return json.load(f)
        
    def save_memories(self):
        """
        Write the current memory data back to the JSON file.
        """
        with open(self.memory_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)
            
    def add_memory(self, content: str, tags: list = None):
        """
        Add a new memory entry with timestamp and optional tags.
        Example:
            add_memory("GAIA learned the word 'laufen'", ["learning", "language"])
        """
        if tags is None:
            tags = []
            
        new_memory = {
            "timestamp": datetime.now().isoformat(timespec='seconds'),
            "content": content,
            "tags": tags
        }
        
        self.data["memories"].append(new_memory)
        self.save_memories()
        
    def get_recent_memories(self, limit: int = 5) -> list:
        """
        Retrieve the most recent memory entries.
        """
        return self.data["memories"][-limit:]