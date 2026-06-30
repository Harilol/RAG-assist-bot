# 📚 Knowledge Assist

> **RAG-powered Document Question Answering System** — Upload a PDF, ask questions in natural language, get context-aware answers grounded in the document.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-yellow)](https://langchain.com)
[![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)](https://www.trychroma.com)
[![LLM](https://img.shields.io/badge/LLM-Groq%20Llama--3.3--70b-green)](https://groq.com)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker)](https://docker.com)
[![Deploy](https://img.shields.io/badge/Deployed-Railway-0B0D0E?logo=railway)](https://railway.app)

---

## 🔎 What is this?

**Knowledge Assist** is a Retrieval-Augmented Generation (RAG) application that lets you interact with PDF documents conversationally.

Instead of manually searching through lengthy documents, just upload a PDF and ask questions in plain English. The app retrieves the most relevant sections using semantic vector search and grounds the LLM's response in that retrieved context — giving fast, context-aware answers with significantly fewer hallucinations than a standalone LLM.

---

## 🏗️ Architecture

```
                User Uploads PDF
                        │
                        ▼
               PDF Text Extraction
                        │
                        ▼
               Recursive Chunking
                        │
                        ▼
            Sentence Embeddings
                        │
                        ▼
              Chroma Vector Store
                        │
────────────────────────────────────────
                        │
                  User Question
                        │
                        ▼
             Similarity Search (Top-K)
                        │
                        ▼
             Retrieved Context + Prompt
                        │
                        ▼
                 Groq Llama 3.3 70B
                        │
                        ▼
               Context-Aware Answer
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 **PDF Upload** | Upload any document directly via the web interface |
| 🧠 **RAG Pipeline** | Retrieval-Augmented Generation grounds answers in actual document content |
| 🔍 **Semantic Search** | Top-K similarity search retrieves only the most relevant chunks |
| 🤖 **Groq-Powered** | Fast inference via Llama 3.3 70B |
| 📚 **Persistent Vector Store** | ChromaDB saves embeddings to disk — no re-processing on restart |
| ⚡ **FastAPI Backend** | Lightweight, fast, production-ready API layer |
| 🐳 **Dockerized** | Fully containerized for easy deployment anywhere |
| ☁️ **Live Deployment** | Deployed and running on Railway |

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Backend | FastAPI |
| Language | Python 3.10+ |
| LLM | Groq — `llama-3.3-70b` |
| RAG Framework | LangChain |
| Vector Database | ChromaDB (persistent) |
| Embeddings | HuggingFace Sentence Transformers |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Docker, Railway |

---

## 📁 Project Structure

```
knowledge-assist/
│
├── app/
│   ├── api/
│   ├── chunking/
│   ├── database/
│   ├── embeddings/
│   ├── loaders/
│   └── main.py
│
├── static/
├── templates/
├── data/
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Harilol/RAG-assist-bot.git
cd RAG-assist-bot
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Create a `.env` file in the root directory:

```bash
GROQ_API_KEY="your-groq-api-key-here"
```

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

Open `http://localhost:8000`, upload a PDF, and start asking questions!

---

## 🐳 Docker

**Build:**
```bash
docker build -t knowledge-assist .
```

**Run:**
```bash
docker run -p 8000:8000 knowledge-assist
```

---

## ☁️ Deployment

The application is containerized with Docker and deployed on **Railway**.

---

## 🔮 Roadmap

- [ ] Multi-document support
- [ ] Persistent chat history
- [ ] Streaming responses
- [ ] User authentication
- [ ] Source citations for retrieved chunks
- [ ] Multiple vector database options
- [ ] Hybrid search (keyword + semantic)
- [ ] Cloud object storage for uploaded files

---

## 🧑‍💻 Author

**Harilol (Narasimha Reddy)**
Final-year B.Tech AI & Data Science | Aspiring Agentic AI Engineer

[GitHub](https://github.com/Harilol) · [LinkedIn](https://linkedin.com/in/narasimha-reddy291204)

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

*Built with FastAPI + LangChain + ChromaDB + Groq*
