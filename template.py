import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "app.py",
    "config.py",
    "utils/__init__.py",
    "utils/groq_client.py",
    "utils/query_executor.py",
    "utils/simulator.py",
    "utils/doc_parser.py",
    "utils/risk_monitor.py",
    "utils/regulatory_qa.py",
    "data/transaction_logs.csv",  # You can keep this empty or add mock CSV
    "data/regulatory_docs/.gitkeep",  # Placeholder for folder creation
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            if filename == ".gitkeep":
                f.write("")  # Keep folder tracked by git
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
