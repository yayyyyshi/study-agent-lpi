import subprocess

# --- Simulated LPI tool calls (replace later if needed) ---
def query_lpi_tool_1(query):
    return f"Concept explanation related to: {query}"

def query_lpi_tool_2(query):
    return f"Practice examples and strategies for: {query}"

# --- Run local LLM using Ollama ---
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
    tool1_data = query_lpi_tool_1(user_input)
    tool2_data = query_lpi_tool_2(user_input)

    combined_prompt = f"""
    A student says: {user_input}

    Tool 1 data: {tool1_data}
    Tool 2 data: {tool2_data}

    1. Identify weaknesses
    2. Suggest improvement plan
    3. Recommend study strategy
    Keep it simple and actionable.
    """

    llm_output = run_llm(combined_prompt)

    return {
        "analysis": llm_output,
        "sources": ["LPI Tool 1", "LPI Tool 2"]
    }

# --- Run agent ---
if __name__ == "__main__":
    user_input = input("Enter your study problem: ")
    result = study_agent(user_input)

    print("\n=== ANALYSIS ===")
    print(result["analysis"])
    print("\n=== SOURCES USED ===")
    print(result["sources"])