import subprocess

# --- Simulated LPI tool calls ---
def smile_overview():
    return "Retrieved data from smile_overview: structured learning framework"

def query_knowledge(topic):
    return f"Retrieved data from query_knowledge: concepts related to {topic}"

# --- LLM call using Ollama ---
def run_llm(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout

# --- Main agent ---
def study_agent(user_input):
    # Query tools
    data1 = smile_overview()
    data2 = query_knowledge(user_input)

    # Combine prompt
    prompt = f"""
    User problem: {user_input}

    Tool Data:
    {data1}
    {data2}

    Analyze the weakness and suggest improvement plan.
    Explain your reasoning clearly.
    """

    # LLM processing
    response = run_llm(prompt)

    return {
        "analysis": response,
        "sources": ["smile_overview", "query_knowledge"]
    }

# --- Run agent ---
if __name__ == "__main__":
    user_input = input("Enter your study problem: ")
    result = study_agent(user_input)

    print("\n=== ANALYSIS ===")
    print(result["analysis"])

    print("\n=== SOURCES USED ===")
    print(result["sources"])