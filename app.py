import streamlit as st
from utils.groq_client import ask_llm
from utils.query_executor import execute_natural_query
from utils.simulator import simulate_policy_change
from utils.doc_parser import summarize_document
from utils.risk_monitor import get_risk_summary
from utils.regulatory_qa import answer_regulatory_question

st.set_page_config(page_title="GenAI FinTech Analyst", layout="wide")
st.title("🧠 GenAI FinTech Analyst for StackIntel")

menu = st.sidebar.selectbox("Choose Feature", [
    "Natural Language Query",
    "Simulate Policy Change",
    "Upload & Summarize Documents",
    "Risk Summary from Logs",
    "Ask Regulatory Questions"
])

if menu == "Natural Language Query":
    st.header("🔍 Ask Transaction Questions")
    question = st.text_input("Enter your question")
    if question:
        result = execute_natural_query(question)
        st.write(result)

elif menu == "Simulate Policy Change":
    st.header("🧪 Simulate Card Policy Change")
    policy_input = st.text_area("Describe the change (e.g., 'set daily limit to ₹50,000')")
    if st.button("Simulate"):
        simulation = simulate_policy_change(policy_input)
        st.write(simulation)

elif menu == "Upload & Summarize Documents":
    st.header("📄 Upload and Summarize Report or KYC")
    uploaded_doc = st.file_uploader("Upload document", type=["pdf", "docx"])
    if uploaded_doc:
        summary = summarize_document(uploaded_doc)
        st.write(summary)

elif menu == "Risk Summary from Logs":
    st.header("⚠️ Risk Behavior Summary")
    summary = get_risk_summary()
    st.write(summary)

elif menu == "Ask Regulatory Questions":
    st.header("📚 Ask Regulation Copilot")
    query = st.text_input("Ask a regulatory or compliance-related question")
    if query:
        response = answer_regulatory_question(query)
        st.write(response)