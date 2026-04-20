# 📚 Study Weakness Analyzer Agent

## 🚀 Overview

This project is an AI-powered agent that analyzes a student’s learning weaknesses and provides actionable improvement strategies.

The agent combines:

* Structured knowledge from LPI tools
* Reasoning from a local LLM (llama3 via Ollama)

It produces explainable outputs by clearly linking recommendations to retrieved data.

---

## 🎯 Features

* Accepts user study problems as input
* Retrieves relevant knowledge using LPI tools
* Processes results using a local LLM
* Generates:

  * Weakness analysis
  * Improvement plan
  * Study strategy
* Provides explainable outputs with reasoning

---

## 🧠 How It Works

1. User provides input (e.g., difficulty in data structures)
2. Agent queries:

   * `smile_overview`
   * `query_knowledge`
3. Data is retrieved from tools
4. Combined input is passed to the LLM
5. LLM generates structured output with reasoning

---

## ▶️ How to Run

```bash
python agent.py
```

---

## 🧪 Example

### Input

I struggle with data structures, especially trees and graphs.

---

### Output

Weakness:

* Difficulty applying concepts to problems

Plan:

* Practice BFS/DFS
* Solve 3 problems daily

Reason:

* Based on data retrieved from LPI tools

---

## 📌 Explainability

The agent explains recommendations **because** it uses outputs retrieved from LPI tools like `smile_overview` and `query_knowledge`.

---

## 🛠️ Tech Stack

* Python
* Ollama (llama3)
* Subprocess execution
* Simulated LPI tool calls

---

## 🔮 Future Improvements

* Integrate real LPI APIs
* Track user learning progress
* Add visualization dashboard

---

## 📎 Purpose

Built as part of the LifeAtlas LPI Level 3 Challenge to demonstrate:

* Agent design
* Tool + LLM integration
* Explainable AI systems
