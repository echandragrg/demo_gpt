from fastapi import FastAPI, File, UploadFile
import PyPDF2
import pandas as pd
import faiss
import numpy as np
from pydantic import BaseModel
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

# For simplicity, we store embeddings in memory
embeddings = []
chunks_text = []

class Query(BaseModel):
    question: str

# Upload file endpoint
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global embeddings, chunks_text
    embeddings = []
    chunks_text = []

    # Read PDF
    if file.filename.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file.file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    # Read CSV/Excel
    elif file.filename.endswith(".csv"):
        df = pd.read_csv(file.file)
        text = df.to_string()
    elif file.filename.endswith((".xls", ".xlsx")):
        df = pd.read_excel(file.file)
        text = df.to_string()
    else:
        return {"error": "Unsupported file type"}

    # Chunk text (simple 500 char chunks)
    chunk_size = 500
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        chunks_text.append(chunk)
        # Create a simple embedding with text length (replace with real embedding model later)
        vec = np.random.rand(512).astype("float32")  # placeholder vector
        embeddings.append(vec)

    # Initialize FAISS index
    global index
    index = faiss.IndexFlatL2(512)
    index.add(np.array(embeddings))

    return {"message": f"File {file.filename} uploaded and processed.", "chunks": len(chunks_text)}

# Ask question endpoint (with retrieval)
@app.post("/ask")
def ask_question(query: Query):
    global index, chunks_text

    # Convert question to vector (placeholder)
    q_vec = np.random.rand(512).astype("float32")

    # Retrieve top 3 chunks
    D, I = index.search(np.array([q_vec]), k=3)
    context = "\n".join([chunks_text[i] for i in I[0]])

    prompt = f"""
You are a helpful AI assistant.
Use the following context to answer the question:
{context}

Question: {query.question}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )
        result = response.json()
        return {"answer": result.get("response", "No response from model.")}

    except Exception as e:
        return {"error": str(e)}