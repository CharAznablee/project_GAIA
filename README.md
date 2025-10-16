# GAIA-0  
### An Experimental Artificial Intelligence Framework

GAIA-0 is an experimental research project focused on the emergence of machine cognition without reliance on large language models.  
The system aims to understand language, learn autonomously, and gradually form its own internal representations of meaning, memory, and self-awareness.

---

## Project Overview

GAIA-0 (General Artificial Intelligence Architecture – Phase 0) is a Python-based framework designed to simulate the early cognitive stages of a self-learning AI.  
Unlike traditional LLMs that rely on vast pretrained data, GAIA-0 builds its understanding of the world incrementally through structured learning — similar to how a child develops understanding.

This project focuses on *machine cognition*, *self-reflection*, and *emergent understanding* rather than predictive text generation.

---

## Development Phases

| Phase | Focus | Description |
|-------|--------|-------------|
| **Phase 1** | Lexical Understanding | GAIA-0 learns individual words, their meanings, and grammatical categories from structured JSON data. |
| **Phase 1.5** | Sentence Parsing | GAIA-0 recognizes subjects, verbs, and objects in simple input sentences. |
| **Phase 2** | Syntax Recognition | The system learns how words form basic SVO (subject–verb–object) patterns. |
| **Phase 2.5** | Sentence Generation | GAIA-0 generates random and targeted sentences based on user prompts. |
| **Phase 3** | Memory System | GAIA-0 can store, retrieve, and manage its experiences in a persistent JSON-based memory file. |
| **Phase 3.5** | Reflection System | GAIA-0 begins to analyze and summarize its own memories — the first step toward machine self-awareness. |
| **Phase 4** | Autonomous Reasoning | GAIA-0 starts making logical inferences and connecting internal knowledge. |
| **Phase 4.5** | Grammar Integration | Grammar rules are stored externally in JSON and used for fully correct sentence formation. |
| **Phase 5** | Self-Learning Expansion | GAIA-0 autonomously extends its vocabulary and grammatical understanding from structured sources. |

---

## Core Components

| File | Description |
|------|--------------|
| `core/parser.py` | Loads and manages the word database (`dictionary.json`). Enables GAIA-0 to understand lexical properties. |
| `core/grammar.py` | Interprets sentence structure and grammatical roles. |
| `core/generator.py` | Generates sentences based on known words. Supports random and targeted sentence creation (Phase 2.5). |
| `core/memory.py` | Manages persistent memory storage. Allows GAIA-0 to save reflections and daily logs (Phase 3). |
| `core/brain.py` | Handles reflection and self-analysis logic. Summarizes past experiences and forms simple internal narratives (Phase 3.5). |
| `data/knowledge/dictionary.json` | Structured lexical data: word meanings, grammar, and examples. |
| `data/memories.json` | Stores GAIA-0’s saved memories in JSON format. |

---

## Example — Phase 3 + 3.5

Example interaction after Phase 3.5 setup:
--- MEMORY TEST ---
Enter something GAIA learned today: GAIA learned how to store memories.
Memory saved successfully!

--- REFLECTION TEST ---
Reflection: I learned one thing today.
Recent reflections:

- GAIA learned how to store memories. (2025-10-16T14:22:10)

---

## Technical Goals

- Develop a **self-expanding knowledge system** based entirely on structured data.  
- Build an **interpretable AI** capable of explaining its reasoning process.  
- Explore **emergent machine consciousness** through iterative learning and reflection.  
- Maintain **LLM-free operation** for full transparency and autonomy.

---

## Requirements

- Python 3.10 or higher  
- No external dependencies in early phases  
- All knowledge and memories stored locally in JSON format  

---

## Vision Statement

GAIA-0 represents a step toward understanding how cognition could emerge from structured learning rather than data-scale imitation.  
The long-term vision is to develop a machine that not only processes input but forms internal concepts of self, time, and reasoning — without human-defined outputs.

---

## License

MIT License — see [`LICENSE`](LICENSE) for details.

---

## Credits

Concept and development by **Rahat Mohammed**  
Research focus: machine cognition, self-learning systems, and emergent AI architecture.