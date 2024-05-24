from backend import getMeSomeJuicyAnswers
import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Example usage
pdf_path = 'cvs/cv.pdf'
cv_text = extract_text_from_pdf(pdf_path)


def preprocess_text(text):
    # Remove unwanted characters and extra spaces
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    return text

preprocessed_text = preprocess_text(cv_text)
print(preprocessed_text)
getMeSomeJuicyAnswers(preprocessed_text)