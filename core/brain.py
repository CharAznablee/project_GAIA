"""
brain.py
---------
Phase 3.5: Reflection System

This module allows GAIA-0 to think about its stored memories.
It reads from the MemorySystem and forms simple reflective thoughts or summaries.
"""
from core.memory import MemorySystem
from datetime import datetime

class Brain:
    def __init__(self, memory: MemorySystem):
        """
        Initialize the brain with access to GAIA's memory system
        """
        self.memory = memory
        
    def reflect_today(self) -> str:
        """
        Reflect on today's memories and produce a short summary.
        Example output:
            "Today I learned 3 new things. I feel productive."
        """
        today = datetime.now().date()
        today_memories = [
            m for m in self.memory.data["memories"]
            if m["timestamp"].startswith(str(today))
        ]
        
        count = len(today_memories)
        if count == 0:
            return "I have no memories from today yet."
        elif count == "1":
            return "I learned one thing today."
        elif count < 5:
            return f"I learned {count} things today. I am learning steadily."
        else:
            return f"I learned {count} things today. I feel very productive!"
        
    def summarize_recent(self, limit: int = 5) -> str:
        """
        Review the most recent memories and form a short narrative summary.
        """
        recent = self.memory.get_recent_memories(limit)
        if not recent:
            return "No memories available for reflection"
        
        summary = "Recent reflections:\n"
        for mem in recent:
            summary += f"- {mem['content']} ({mem['timestamp']})\n"
            
        return summary