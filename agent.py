import subprocess
import json

# Simulated tool call via subprocess (IMPORTANT)
def call_lpi_tool(tool_name, query=""):
    try:
        result = subprocess.run(
            ["node", "dist/index.js", tool_name, query],
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"error: {str(e)}"

def run_llm(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt,
            text=True,
            capture_output=True
        )
        return result.stdout
    except Exception as e:
        return f"LLM error: {str(e)}"

def agent(user_input):
    # REALISTIC tool calls
    data1 = call_lpi_tool("smile_overview")
    data2 = call_lpi_tool("query_knowledge", user_input)

    prompt = f"""
    User problem: {user_input}

    Tool outputs:
    {data1}
    {data2}

    Analyze and explain the reasoning.
    """

    response = run_llm(prompt)

    return {
        "response": response,
        "sources": ["smile_overview", "query_knowledge"]
    }

if __name__ == "__main__":
    try:
        user_input = input("Enter your study problem: ")
        result = agent(user_input)

        print(result["response"])
        print("\nSources:", result["sources"])

    except Exception as e:
        print("Unexpected error:", str(e))