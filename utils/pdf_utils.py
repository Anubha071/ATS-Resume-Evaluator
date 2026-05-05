# reading the pdf file and extracting text from it.
from PyPDF2 import PdfReader

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)   # It gives list of pages(page1, page2, page3...) in the pdf file, and we can iterate through them to extract text.
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
