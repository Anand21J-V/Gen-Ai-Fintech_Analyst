# app.py
import streamlit as st
import pandas as pd
from utils.groq_client import ask_llm
from utils.query_executor import execute_natural_query
from utils.simulator import simulate_policy_change
from utils.doc_parser import summarize_document
from utils.risk_monitor import get_risk_summary
from utils.regulatory_qa import answer_regulatory_question

st.set_page_config(page_title="GenAI FinTech Analyst", layout="wide")

# Sidebar
st.sidebar.image("image.png", width=120)
st.sidebar.markdown("🚀 **AI-Powered Analyst for B2B Transactions**")
st.sidebar.markdown("Crafted by **Anand Vishwakarma**")

st.title("🧠 GenAI FinTech Analyst")

# Tabs for features
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔍 Natural Language Query",
    "🧪 Simulate Policy",
    "📄 Document Summary",
    "⚠️ Risk Monitor",
    "📚 Regulatory Q&A"
])

# TAB 1: Transaction Questions
with tab1:
    st.subheader("Ask questions about your transaction logs")
    st.markdown("Example: `What is the average transaction value for March 2024?`")
    question = st.text_input("🔎 Enter your query")

    if question:
        # Save question in session state
        st.session_state.question = question
        result = execute_natural_query(question)
        st.success("✅ LLM Analysis Complete")
        st.markdown(f"**📌 Response:**\n\n{result}")
        with st.expander("📊 Preview Transaction Data"):
            df = pd.read_csv("data/transaction_logs.csv")
            st.dataframe(df.head())

# TAB 2: Simulate Policy Change
with tab2:
    st.subheader("Describe a transaction policy to simulate its impact")
    st.markdown("Example: `Set daily card limit to ₹50,000`")
    policy_input = st.text_area("✏️ Describe your policy change here")
    
    if st.button("🚀 Simulate"):
        # Save policy input in session state
        st.session_state.policy_input = policy_input
        simulation = simulate_policy_change(policy_input)
        st.success("✅ Simulation Result")
        st.markdown(simulation)

# TAB 3: Document Upload and Summary
with tab3:
    st.subheader("Upload PDF/Docx for KYC or report summary")
    uploaded_doc = st.file_uploader("📂 Upload Document", type=["pdf", "docx"])
    
    if uploaded_doc:
        # Save document in session state
        st.session_state.uploaded_doc = uploaded_doc
        summary = summarize_document(uploaded_doc)
        st.success("✅ Summary Generated")
        st.markdown(summary)

# TAB 4: Risk Summary
with tab4:
    st.subheader("High-value transaction behavior and pattern risks")
    if st.button("🛡️ Analyze Risks"):
        summary = get_risk_summary()
        st.success("✅ Risk Analysis Complete")
        st.markdown(summary)
        with st.expander("📊 High-Value Transactions"):
            df = pd.read_csv("data/transaction_logs.csv")
            st.dataframe(df[df['amount'] > 100000])

# TAB 5: Regulatory Q&A
with tab5:
    st.subheader("Ask regulation-based questions")
    st.markdown("Example: `Is Aadhaar mandatory for KYC?`")
    query = st.text_input("📘 Enter regulatory question")
    
    if query:
        # Save query in session state
        st.session_state.query = query
        response = answer_regulatory_question(query)
        st.success("✅ Regulation Answer")
        st.markdown(response)

# Footer
st.markdown("---")
st.markdown("Built with 💡 by **Anand Vishwakarma** | Powered by **LLaMA 3.3 via Groq**")

# utils/groq_client.py
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

# utils/simulator.py
from utils.groq_client import ask_llm

def simulate_policy_change(policy):
    prompt = f"Assume a card usage policy system. Simulate the impact of this policy change: {policy}. Give possible pros/cons based on card usage patterns."
    return ask_llm(prompt)

# utils/doc_parser.py
import PyPDF2

def summarize_document(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    from utils.groq_client import ask_llm
    return ask_llm(f"Summarize and extract key clauses: {text[:3000]}")

# utils/risk_monitor.py
import pandas as pd
from utils.groq_client import ask_llm

def get_risk_summary():
    df = pd.read_csv("data/transaction_logs.csv")
    suspicious = df[df['amount'] > 100000]
    text = suspicious.to_string(index=False)
    prompt = f"Summarize these high-value transactions for potential risks: {text[:3000]}"
    return ask_llm(prompt)

# utils/regulatory_qa.py
from utils.groq_client import ask_llm
import os

def answer_regulatory_question(query):
    docs = " ".join([open(f"data/regulatory_docs/{f}").read() for f in os.listdir("data/regulatory_docs") if f.endswith(".txt")])
    prompt = f"Based on these regulations: {docs[:4000]}, answer: {query}"
    return ask_llm(prompt)

