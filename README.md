# 📘 Research RAG Assistant

*A retrieval-augmented language model for academic question-answering.*

This project builds a small research assistant that can read a collection of academic papers and answer questions about them. It uses a classic RAG pipeline: the documents are split into meaningful chunks, embedded into a vector store, and retrieved on demand to ground the model’s answers.

The goal is simple: give an LLM access to your papers so it can answer domain-specific questions more reliably.

---

## 🧠 What This Project Does

* Loads PDFs (papers, theses, reports) and breaks them into clean text chunks.
* Creates embeddings and stores them in a local vector database (Chroma).
* Retrieves the most relevant pieces of text for each query.
* Sends both the question and retrieved context to a language model.
* Returns grounded answers instead of hallucinations.
* Includes a minimal Streamlit interface for interaction.

You can drop any set of research papers into the `data/` folder and instantly query them.

---

## 🏗️ Project Structure

```
rag_assistant/
│
├── data/                     # PDFs go here
├── chroma_store/             # Vector database (created after embedding)
│
├── src/
│   ├── ingest.py             # Load PDFs and chunk text
│   ├── embed.py              # Build embeddings + vector DB
│   ├── retrieve.py           # RAG pipeline: retrieve + answer
│   └── app.py                # Streamlit interface
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd rag_assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Add your OpenAI key:

```
export OPENAI_API_KEY="your_key_here"
```

(You can also use a `.env` file if you prefer.)

---

## 📥 Step 1 — Add Your PDFs

Place any research PDFs you want to query inside:

```
data/
```

That’s it. The pipeline will handle the rest.

---

## 🔧 Step 2 — Build the Vector Database

Run:

```bash
python src/embed.py
```

This will:

* Load your PDFs
* Split them into overlapping chunks
* Create embeddings
* Write everything to `chroma_store/`

You do this once unless you change the documents.

---

## 🔍 Step 3 — Ask Questions

At the command line:

```bash
python src/retrieve.py
```

Or inside Python:

```python
from retrieve import ask_question
print(ask_question("What are common methods for fine-tuning transformer models?"))
```

The assistant will answer using only the information it retrieved from your papers.

---

## 💬 Streamlit Interface (Optional UI)

Run the simple UI:

```bash
streamlit run src/app.py
```

You’ll see a small web page where you can type questions and view answers.

---

## 🧪 How It Works (Short Explanation)

1. **Chunking**
   Academic PDFs often contain long paragraphs. We split them into overlapping 1000-character chunks so retrieval works well.

2. **Embedding**
   Each chunk is turned into a high-dimensional vector using an embedding model.

3. **Vector Store (Chroma)**
   All vectors are stored locally and indexed for fast retrieval.

4. **Retrieval**
   For any question, the top-k similar chunks are selected.

5. **Generation**
   These chunks, along with the question, are passed to the LLM to produce an answer that is grounded in your documents.

---

## 📊 Example Query

**Question:**
“What are the major challenges in applying LLMs in low-resource domains?”

**Answer (shortened):**
Models often require high-quality supervised data, which low-resource domains lack. This affects fine-tuning, evaluation, and the reliability of generated text. Approaches such as instruction tuning, retrieval augmentation, and domain-adaptive pretraining are commonly proposed in the literature.

*(The exact answer depends on the documents you provide.)*

---

## 📎 Notes for Reviewers / Recruiters

This project demonstrates:

* Document processing
* Embedding models and retrieval
* LLM integration
* Use of LangChain and Chroma
* Basic UI deployment
* Clear, reproducible code design
* Research-oriented workflow (chunking → retrieval → evaluation)

---

## 📌 Future Work

* Add evaluation (retrieval accuracy, recall@k).
* Experiment with different embedding models.
* Add metadata filters (author, year, topic).
* Deploy to Hugging Face Spaces.
* Build an automatic summarization mode.

---

If you want, I can now prepare a **GitHub Repository Description**, **short tagline**, or **CV bullet point** that describes this project concisely and professionally.
