from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma

def ask_question(question):
    db = Chroma(persist_directory="chroma_store")
    retriever = db.as_retriever(search_kwargs={"k": 3})
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    qa = RetrievalQA.from_chain_type(
        llm=model,
        retriever=retriever,
        chain_type="stuff"
    )
    result = qa.run(question)
    return result

if __name__ == "__main__":
    print(ask_question("Summarize the main methods used for transformer fine-tuning."))
