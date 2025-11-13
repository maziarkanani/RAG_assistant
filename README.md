# 📘 Research RAG Assistant  
A retrieval-augmented language model for academic question-answering.

This project builds a small research assistant that can read a collection of academic papers and answer questions about them. It uses a classic RAG pipeline: the documents are split into meaningful chunks, embedded into a vector store, and retrieved on demand to ground the model’s answers.

The goal is simple: give an LLM access to your papers so it can answer domain-specific questions more reliably.

## 🧠 What This Project Does
- Loads PDFs (papers, theses, reports) and breaks them into clean text chunks.
- Creates embeddings and stores them in a local vector database (Chroma).
- Retrieves the most relevant pieces of text for each query.
- Sends both the question and retrieved context to a language model.
- Returns grounded answers instead of hallucinations.
- Includes a minimal Streamlit interface for interaction.

## 🏗️ Project Structure
```
rag_assistant/
│
├── data/
├── chroma_store/
│
├── src/
│   ├── ingest.py
│   ├── embed.py
│   ├── retrieve.py
│   └── app.py
│
├── requirements.txt
└── README.md
```

## 🛠️ Installation
```bash
pip install -r requirements.txt
```

Add your OpenAI API key:
```bash
export OPENAI_API_KEY="your_key_here"
```

## 📥 Step 1 — Add Your PDFs
Place PDFs inside:
```
data/
```

## 🔧 Step 2 — Build Vector DB
```bash
python src/embed.py
```

## 🔍 Step 3 — Ask Questions
```bash
python src/retrieve.py
```

Or:
```python
from retrieve import ask_question
print(ask_question("Summarize transformer fine-tuning methods."))
```

## 💬 Streamlit UI
```bash
streamlit run src/app.py
```

## 📊 Example
**Q:** What are major challenges in applying LLMs?  
**A:** Depends on retrieved documents; typically data scarcity, evaluation, and domain adaptation issues.

## 📌 Future Work
- Retrieval evaluation
- Different embedding models
- Metadata filters
- Deployment
