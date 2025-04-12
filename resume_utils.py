import subprocess
import fitz
import spacy
import streamlit as st

@st.cache_resource
def load_model():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"], check=True)
        return spacy.load("en_core_web_sm")
    

nlp = load_model()

skills_list = ['python', 'sql', 'machine learning', 'excel', 'power bi', 'deep learning']

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def preprocess(text,nlp):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def extract_skills(text, skills_list):
    return [skill for skill in skills_list if skill in text.lower()]
