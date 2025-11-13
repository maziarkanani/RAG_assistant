import streamlit as st
from retrieve import ask_question

st.title("🧠 Research RAG Assistant")
st.write("Ask questions about your uploaded papers.")

question = st.text_input("Enter your question:")
if st.button("Ask"):
    with st.spinner("Thinking..."):
        answer = ask_question(question)
        st.markdown(f"**Answer:** {answer}")
