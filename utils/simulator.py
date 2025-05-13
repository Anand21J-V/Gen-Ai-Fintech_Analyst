from utils.groq_client import ask_llm

def simulate_policy_change(policy):
    prompt = f"Assume a card usage policy system. Simulate the impact of this policy change: {policy}. Give possible pros/cons based on card usage patterns."
    return ask_llm(prompt)