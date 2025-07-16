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





# ---------- Step 3: Upload PDF files ----------
with st.sidebar:
    st.header("📁 Upload PDFs")
    pdf_docs = st.file_uploader("Choose PDF files", type=["pdf"], accept_multiple_files=True)





# ---------- Step 4: Text Extraction & Chunking ----------
if pdf_docs:
    raw_text = get_pdf_text(pdf_docs)
    st.success("✅ Text extracted from PDFs.")
    st.write(raw_text[:1000])