# ChandraGPT 🤖 – Local AI Assistant

ChandraGPT is a **local AI assistant** that can answer questions in natural language and read uploaded files (PDF, CSV, Excel) to provide context-aware responses. It uses a **local LLM (Mistral via Ollama)**, a **FastAPI backend**, and a **Streamlit frontend**.

---

## Features

- Ask questions and get AI-generated answers.
- Upload files (PDF, CSV, XLS/XLSX) for context-aware responses.
- Retrieval-Augmented Generation (RAG) workflow:
  - Extract text from uploaded files.
  - Chunk and store content in FAISS vector database.
  - Retrieve relevant sections to answer queries.
- Clean, interactive **Streamlit UI**.
- Fully offline, privacy-friendly.

---

## Project Structure


chandra-gpt/
│
├── backend.py # FastAPI backend (handles LLM requests and file processing)
├── frontend.py # Streamlit UI (question input, file upload)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## Prerequisites

1. **Python 3.10+**
2. **Ollama** – Local LLM runner  
   - Install: [https://ollama.com](https://ollama.com)  
   - Pull Mistral model:  
     ```bash
     ollama pull mistral
     ```
3. Install required Python packages:

```bash
python -m pip install -r requirements.txt
Setup & Run
1️⃣ Start Ollama
ollama run mistral

Keep Ollama running. This is the local LLM server.

2️⃣ Start Backend
python -m uvicorn backend:app --reload

Backend runs at: http://127.0.0.1:8000/

Test API with Swagger UI: http://127.0.0.1:8000/docs

3️⃣ Start Frontend
python -m streamlit run frontend.py

Streamlit UI opens in browser at: http://localhost:8501

How to Use

Upload a File (optional)

Supported formats: PDF, CSV, XLS/XLSX.

The backend extracts text, chunks it, and stores it in FAISS for retrieval.

Ask a Question

Type your question in the input box.

Click Submit.

The AI responds using uploaded file context (if any) and default knowledge.

Technology Stack

Backend: FastAPI

Frontend: Streamlit

Local LLM: Mistral via Ollama

Vector DB: FAISS (for retrieving file content)

File Parsing: PyPDF2, pandas

Next-Level Improvements

Replace placeholder embeddings with real embeddings (e.g., sentence-transformers) for better context relevance.

Add conversation memory to maintain context across multiple questions.

Handle large PDFs efficiently.

Implement streaming responses from the LLM.

Example Workflow

Upload a PDF with “German A1 vocabulary.”

Ask: “What are the top 10 verbs in this PDF?”

ChandraGPT retrieves relevant content and generates a concise answer using Mistral.

Tips for Users

Ensure Ollama is running before starting the backend.

For large files, initial processing may take a few seconds.

Use Chrome or Edge for best Streamlit experience.

License

Educational and personal use only.

Author: Chandra Bahadur Gurung
GitHub/Portfolio: [Your GitHub link here]


---

If you want, I can also **make an enhanced GitHub README** version with:

- Badges (Python version, Streamlit, FastAPI)  
- Screenshot of Streamlit UI  
- Example curl/Postman request  

This makes your project **look professional and portfolio-ready**.  

Do you want me to do that next?
