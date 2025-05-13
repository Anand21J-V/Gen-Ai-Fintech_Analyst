from utils.groq_client import ask_llm
import os

def answer_regulatory_question(query):
    docs = " ".join([open(f"data/regulatory_docs/{f}").read() for f in os.listdir("data/regulatory_docs") if f.endswith(".txt")])
    prompt = f"Based on these regulations: {docs[:4000]}, answer: {query}"
    return ask_llm(prompt)