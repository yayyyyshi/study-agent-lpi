# HOW I DID IT

## My Approach

I decided to build a Study Weakness Analyzer Agent because it directly connects to my idea of a digital twin that tracks learning patterns. My goal was to create something practical that helps identify weaknesses and improve study strategies.

## Steps I Followed

* Created a separate repository for Level 3
* Built a Python-based agent structure
* Simulated LPI tool calls like smile_overview and query_knowledge
* Integrated a local LLM using Ollama (llama3)
* Used subprocess to connect the agent with the LLM
* Designed the flow to combine tool outputs and generate a response

## Problems I Faced

One challenge was understanding how to properly structure the agent so that tool outputs and LLM reasoning worked together. Initially, I tried simple print-based outputs, but I realized that wasn’t enough to simulate real agent behavior.

I also faced issues running Ollama in VS Code due to PATH problems, which I solved by restarting the environment.

## How I Solved Them

I switched to a subprocess-based approach for running the LLM, which made the integration cleaner and more reliable. I also refined how tool outputs were passed into the prompt to make the response more structured.

## What I Learned

I learned how agents combine structured data with LLM reasoning to produce meaningful outputs. I also understood the importance of explainability — not just giving answers, but explaining why those answers are generated.

## What I Would Improve

If I had more time, I would connect real LPI APIs instead of simulated responses and add memory to track user progress over time.
