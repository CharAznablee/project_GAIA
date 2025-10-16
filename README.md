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
| **Phase 1.5** | Sentence Testing | Simple Subject–Verb–Object sentences are tested and recognized. |
| **Phase 2** | Syntax Recognition | The system learns how words form simple sentences (SVO). |
| **Phase 2.5** | Extended Syntax | Additional sentence structures and grammar hints are integrated. |
| **Phase 3** | Memory & Reflection | Daily memory logs and internal reflection mechanisms are introduced. |
| **Phase 3.5** | Enhanced Memory Testing | Memory storage, recall, and reflection are tested with user prompts. |
| **Phase 4** | Autonomous Reasoning | GAIA-0 starts making logical inferences and connecting internal knowledge. |
| **Phase 4.5** | External Dictionary Integration | GAIA-0 uses large external JSON word lists and grammar rules to detect POS, validate syntax, and learn words automatically. |

---

## Core Components

| File | Description |
|------|--------------|
| `core/parser.py` | Lexicon system: loads local & external dictionaries, POS rules, syntax patterns, and manages learned words. |
| `core/grammar.py` | Grammar system: validates sentence structures, provides grammar hints, integrates with Lexicon. |
| `core/brain.py` | Core cognitive loop (Phase 3+). Handles internal states, thoughts, and reflection. |
| `data/knowledge/dictionary.json` | Structured lexical data: word meanings, grammar, and examples. |
| `data/knowledge/words_dictionary.json` | Large English wordlist (dwyl format). |
| `data/knowledge/pos_rules.json` | POS detection heuristics (suffixes, prefixes, word lists). |
| `data/knowledge/syntax_patterns.json` | Sentence structures for syntax validation. |
| `data/knowledge/grammar_rules.json` | Human-readable grammar hints for each POS. |
| `data/knowledge/learned_words.json` | GAIA-0’s personal lexicon of learned words and POS. |

---

## Technical Goals

- Develop a **self-expanding knowledge system** based entirely on structured data.  
- Build an **interpretable AI** capable of explaining its reasoning process.  
- Explore **emergent machine consciousness** through iterative learning and reflection.  
- Maintain **LLM-free operation** for full transparency and autonomy.  
- Use **external dictionaries** to accelerate learning and POS detection.

---

## Example – Phase 4.5

Example interaction:

Enter a sentence: The Cat is running

[1] Tokenized Sentence:
['The', 'Cat', 'is', 'running']

[2] Detected Parts of Speech:
The → article
Cat → noun
is → to_be_forms
running → verb_ing

[3] Syntax Validation:
[INFO] Syntax pattern matched: article_noun_is_verb_ing

[4] Grammar Hints:
The → Precedes a noun and defines its definiteness. Examples: a, an, the.
Cat → Usually represents a person, place, or thing. Examples: cat, dog, apple.
is → Forms of the verb 'to be', describing states. Examples: is, am, are, was, were.
running → Present participle form of a verb, describing ongoing action. Examples: running, eating.

---

## Requirements

- Python 3.10 or higher  
- No external dependencies in Phase 1–4.5  
- All knowledge stored locally in JSON format  

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