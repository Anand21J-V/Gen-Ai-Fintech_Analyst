import pandas as pd
from utils.groq_client import ask_llm

def execute_natural_query(question):
    df = pd.read_csv("data/transaction_logs.csv")
    cols = ", ".join(df.columns)
    prompt = f"Given the transaction data with columns: {cols}, answer the question: {question}"
    return ask_llm(prompt)

# utils/simulator.py
from utils.groq_client import ask_llm

def simulate_policy_change(policy):
    prompt = f"Assume a card usage policy system. Simulate the impact of this policy change: {policy}. Give possible pros/cons based on card usage patterns."
    return ask_llm(prompt)