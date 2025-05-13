# GenAI FinTech Analyst

## Overview

**GenAI FinTech Analyst** is an AI-powered tool designed to assist financial analysts in analyzing transaction logs, simulating policy changes, summarizing documents, detecting risky behaviors, and answering regulatory questions using advanced natural language processing (NLP) and machine learning (ML) techniques. Built with **Streamlit**, it provides an intuitive, user-friendly interface for performing these tasks efficiently.

The system uses **Groq LLM** (Large Language Model) to process complex queries, and it integrates various functionalities such as querying transaction data, simulating policy impacts, summarizing documents, and analyzing transaction risks.

## Features

### 🔍 **Natural Language Query**
Ask specific questions about transaction logs. For example, "What is the average transaction value for March 2024?" and get an AI-generated response.

### 🧪 **Simulate Policy Change**
Simulate the impact of changes in transaction policies (e.g., setting daily limits) and get predictions about the potential effects on transaction patterns.

### 📄 **Document Summary**
Upload PDFs or DOCX files containing KYC or financial reports, and receive AI-generated summaries that extract key details from the documents.

### ⚠️ **Risk Monitor**
Analyze high-value transactions and detect any risky patterns or behaviors. This feature highlights transactions over a specified threshold and provides risk summaries.

### 📚 **Regulatory Q&A**
Ask questions related to financial regulations or compliance, and the system will generate answers based on existing regulatory documents.

## Project Structure

```

project\_root/
├── app.py                          # Streamlit main app
├── config.py                       # Config for API keys and constants
├── utils/
│   ├── **init**.py
│   ├── groq\_client.py              # Handles Groq LLM client interaction
│   ├── query\_executor.py           # Executes queries on data/logs
│   ├── simulator.py                # Simulates transaction policy impact
│   ├── doc\_parser.py               # Parses and summarizes uploaded documents (PDFs, KYC, reports)
│   ├── risk\_monitor.py             # Monitors logs for risky patterns
│   └── regulatory\_qa.py            # Answers regulatory questions via RAG
└── data/
├── transaction\_logs.csv        # Sample transaction logs
└── regulatory\_docs/            # Directory of PDF/DOCs to use in RAG

````

## Installation

### Prerequisites

To get started, make sure you have the following installed on your machine:

- Python 3.8 or higher
- Git (for cloning the repository)

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/genai-fintech-analyst.git
   cd genai-fintech-analyst
````

2. **Create a virtual environment** (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install required dependencies**:

   Install the dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your configuration file**:

   Create a `config.py` file in the project root directory with the following structure:

   ```python
   GROQ_API_KEY = "your_groq_api_key"
   LLM_MODEL = "llama-3-70b-8192"
   ```

   * Replace `your_groq_api_key` with your actual Groq API key.
   * Modify the model name if needed, based on the model you are using.

5. **Set up `.gitignore`**:

   Make sure your `config.py` file is included in `.gitignore` to prevent exposing sensitive information:

   ```
   config.py
   ```

6. **Run the application**:

   Once everything is set up, you can run the application using:

   ```bash
   streamlit run app.py
   ```

   This will start a local web server and open the app in your browser.

## Usage

1. **Ask Transaction Questions**:

   * In the "Natural Language Query" tab, type a query related to your transaction logs, such as "What is the average transaction value for March 2024?" and press Enter. The system will provide an AI-generated response.

2. **Simulate Policy Changes**:

   * In the "Simulate Policy Change" tab, describe a policy change (e.g., "Set daily card limit to ₹50,000") and click on "Simulate." The system will simulate the policy's impact.

3. **Upload & Summarize Documents**:

   * In the "Upload & Summarize Documents" tab, upload a PDF or DOCX file containing KYC or financial reports. The system will extract key details and generate a summary.

4. **Analyze Transaction Risks**:

   * In the "Risk Summary from Logs" tab, click on "Analyze Risks" to analyze high-value transactions in your dataset. The system will identify any suspicious patterns.

5. **Ask Regulatory Questions**:

   * In the "Regulatory Q\&A" tab, enter a regulatory or compliance-related question, and the system will provide an answer based on regulatory documents.

## Configuration

### Configuration File (`config.py`)

This file stores your API keys and model settings for integration with Groq LLM and other services.

```python
GROQ_API_KEY = "your_groq_api_key"
LLM_MODEL = "llama-3-70b-8192"
```

* Replace `your_groq_api_key` with your Groq API key.
* Adjust the model name if needed (e.g., if you are using a different LLM model).

### `.gitignore`

Ensure the following is in your `.gitignore` to prevent sensitive information from being tracked by Git:

```
config.py
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-xyz`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Added feature xyz'`).
5. Push to the branch (`git push origin feature-xyz`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* **Groq** for providing the LLM for natural language processing.
* **Streamlit** for building the user interface.
* **PyPDF2** for parsing PDF documents.

Built with 💡 by **Anand Vishwakarma** | Powered by **LLaMA 3.3 via Groq**


