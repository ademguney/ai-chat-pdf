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