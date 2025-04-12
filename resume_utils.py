import fitz
import spacy

def load_nlp_model():
    return spacy.load("en_core_web_sm")

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
