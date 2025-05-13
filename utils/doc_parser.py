import PyPDF2

def summarize_document(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    from utils.groq_client import ask_llm
    return ask_llm(f"Summarize and extract key clauses: {text[:3000]}")
