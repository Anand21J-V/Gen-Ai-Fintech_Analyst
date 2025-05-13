import pandas as pd
from utils.groq_client import ask_llm

def get_risk_summary():
    df = pd.read_csv("data/transaction_logs.csv")
    suspicious = df[df['amount'] > 100000]
    text = suspicious.to_string(index=False)
    prompt = f"Summarize these high-value transactions for potential risks: {text[:3000]}"
    return ask_llm(prompt)