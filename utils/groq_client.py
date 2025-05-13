from config import GROQ_API_KEY, LLM_MODEL
import openai

def ask_llm(prompt):
    client = openai.OpenAI(api_key=GROQ_API_KEY, base_url="https://api.groq.com/openai/v1")
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message.content.strip()

# utils/query_executor.py
import pandas as pd
from utils.groq_client import ask_llm

def execute_natural_query(question):
    df = pd.read_csv("data/transaction_logs.csv")
    cols = ", ".join(df.columns)
    prompt = f"Given the transaction data with columns: {cols}, answer the question: {question}"
    return ask_llm(prompt)