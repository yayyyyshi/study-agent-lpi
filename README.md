# 📚 Study Weakness Analyzer Agent

## 🚀 Overview

The **Study Weakness Analyzer Agent** is an AI-powered tool that helps students identify their weak areas and improve their study strategy.

It takes a user’s problem (e.g., difficulty in Data Structures), analyzes it using structured tool inputs, and generates a clear, actionable improvement plan using a local LLM.

---

## 🎯 Features

* Accepts natural language input from users
* Simulates querying multiple LPI tools
* Uses a local LLM (Ollama - llama3) for analysis
* Provides:

  * Weakness breakdown
  * Study plan
  * Learning strategy
* Clearly cites sources used (Explainable AI)

---

## 🧠 How It Works

1. User enters a study-related problem
2. Agent queries:

   * **LPI Tool 1** → Concept understanding
   * **LPI Tool 2** → Practice strategies
3. Data is combined and sent to the LLM
4. LLM generates structured analysis
5. Agent outputs results with sources

---

## 🛠️ Tech Stack

* Python
* Ollama (llama3 local LLM)
* Subprocess module
* Simulated LPI tools (can be replaced with real endpoints)

---

## ▶️ How to Run

```bash
python agent.py
```

---

## 🧪 Example

### 🧾 Input

```
I am struggling with Data Structures, especially trees and graphs. I understand theory but cannot solve problems.
```

---

### 📊 Output

```
=== ANALYSIS ===

Weakness Identified:
- Lack of practical problem-solving experience in trees and graphs
- Difficulty applying theoretical knowledge to coding problems

Improvement Plan:
- Start with basic problems on trees (traversals, BST)
- Practice graph algorithms like BFS and DFS daily
- Use platforms like LeetCode or HackerRank

Study Strategy:
- Break problems into smaller parts
- Practice 3–5 problems daily
- Revise concepts after solving problems

=== SOURCES USED ===
['LPI Tool 1', 'LPI Tool 2']
```

---

## 📌 Explainability

This agent explicitly shows which tools contributed to the final answer:

* LPI Tool 1 → Conceptual understanding
* LPI Tool 2 → Practice strategies

This ensures transparency in how the output is generated.

---

## 🔮 Future Improvements

* Integrate real LPI tool APIs
* Add progress tracking over time
* Personalize recommendations using user history
* Add visualization for learning progress

---

## 📎 Project Purpose

This project was built as part of the **LifeAtlas LPI Level 3 Challenge** to demonstrate:

* Agent design
* Tool + LLM integration
* Explainable AI systems
