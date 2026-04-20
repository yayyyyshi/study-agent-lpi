import subprocess
import json

# --- LPI Tool Caller ---
def call_lpi_tool(tool_name, query=""):
    try:
        result = subprocess.run(
            ["node", "dist/index.js", "tools/call", tool_name, query],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode != 0:
            return f"Error calling {tool_name}: {result.stderr}"

        return result.stdout.strip()

    except Exception as e:
        return f"Exception while calling {tool_name}: {str(e)}"


# --- LLM Runner (Ollama) ---
def run_llm(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt,
            text=True,
            capture_output=True,
            timeout=20
        )

        if result.returncode != 0:
            return f"LLM error: {result.stderr}"

        return result.stdout.strip()

    except Exception as e:
        return f"LLM exception: {str(e)}"


# --- Agent Logic ---
def study_agent(user_input):

    # Input validation (important for robustness)
    if not user_input or not user_input.strip():
        return {
            "analysis": "Please provide a valid study problem.",
            "sources": [],
            "raw_data": {}
        }

    # --- Tool Calls ---
    tool1_data = call_lpi_tool("smile_overview")
    tool2_data = call_lpi_tool("query_knowledge", user_input)

    # Debug / transparency output
    print("\n--- RAW TOOL OUTPUT ---")
    print("\n[smile_overview]:\n", tool1_data[:300])
    print("\n[query_knowledge]:\n", tool2_data[:300])

    # --- Prompt Construction ---
    prompt = f"""
    A student says: "{user_input}"

    Data retrieved from tools:

    smile_overview:
    {tool1_data}

    query_knowledge:
    {tool2_data}

    Based on this data:

    1. Identify the student's weakness
    2. Suggest a clear improvement plan
    3. Explain the reasoning (must reference tool data)

    Keep it simple and actionable.
    """

    # --- LLM Processing ---
    llm_response = run_llm(prompt)

    return {
        "analysis": llm_response,
        "sources": ["smile_overview", "query_knowledge"],
        "raw_data": {
            "smile_overview": tool1_data,
            "query_knowledge": tool2_data
        }
    }


# --- Main Runner ---
if __name__ == "__main__":
    try:
        user_input = input("Enter your study problem: ")

        result = study_agent(user_input)

        print("\n=== ANALYSIS ===")
        print(result["analysis"])

        print("\n=== SOURCES USED ===")
        print(result["sources"])

    except Exception as e:
        print("Unexpected system error:", str(e))