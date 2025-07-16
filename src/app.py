import os
import streamlit as st
from dotenv import load_dotenv

from utils.pdf_utils import get_pdf_text
from utils.qa_chain import get_conversational_chain
from utils.embedding_utils import get_vectorstore, get_text_chunks



# ---------- Step 1: Environment Setup ----------
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    st.error("You need to set an OpenAI API key")
    st.stop()





# ---------- Step 2: Streamlit Page Setup ----------
st.set_page_config(page_title="Open Source Chat", page_icon=":books:", layout="wide")
st.title("PDF Chatbot")
st.write("Please upload your PDF files.")




# ---------- Step 6: Initialize Chat History ----------
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []




# ---------- Step 3: Upload PDF files ----------
with st.sidebar:
    st.header("📁 Upload PDFs")
    pdf_docs = st.file_uploader("Choose PDF files", type=["pdf"], accept_multiple_files=True)





# ---------- Step 4: Text Extraction & Chunking ----------
if pdf_docs:
    raw_text = get_pdf_text(pdf_docs)
    st.success("✅ Text extracted from PDFs.")
    st.write(raw_text[:1000])

    # Chunking
    text_chunks = get_text_chunks(raw_text)
    st.success("✅ Text split into chunks.")

    # Embedding & Vector store
    vectorstore = get_vectorstore(text_chunks)
    st.success("✅ Vector store created.")

    # ---------- Step 5: Ask a Question ----------
    st.subheader("❓ Ask a question")
    user_question = st.text_input("Enter your question")

    if user_question:
        chain = get_conversational_chain(vectorstore= vectorstore)
        result = chain({"query": user_question})
        answer = result.get("result")

        st.subheader("📢 Answer:")
        st.write(answer)

        with st.expander(" Source Documents"):
            for doc in result["source_documents"]:
                st.markdown(doc.page_content)


        # Step 6: Add to chat history
        st.session_state.chat_history.append((user_question, answer))

    # Step 6: Show chat history
    if st.session_state.chat_history:
        st.subheader("💬 Chat History:")
        for i, (question, answer) in enumerate(st.session_state.chat_history, 1):
            st.markdown(f"**Q{i}:** {question}")
            st.markdown(f"**A{i}:** {answer}")

