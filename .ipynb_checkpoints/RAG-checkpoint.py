import streamlit as st
import PyPDF2
import google.generativeai as palm
from dotenv import load_dotenv
import os

# Configure the API key for Google Generative AI
load_dotenv()
api_key = os.environ['api_key']
palm.configure(api_key=api_key)

# Function to extract text from a PDF
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to read text from a text file
def extract_text_from_txt(file_path):
    with open(file_path, 'r') as txt_file:
        return txt_file.read()

# Choose the file to load (PDF or TXT)
file_path = "test.txt"  # or "document.txt" if you're using a text file

# Load the document content
if file_path.endswith('.pdf'):
    document_text = extract_text_from_pdf(file_path)
elif file_path.endswith('.txt'):
    document_text = extract_text_from_txt(file_path)
else:
    st.error("Unsupported file format. Please use a PDF or TXT file.")
    st.stop()

# Function to generate answers based on the content and question
def generate_answer(context, question, model="models/text-bison-001"):
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,  # Fixed temperature for consistency
        max_output_tokens=800,  # You can adjust this as needed
    )
    return completion.result

# Streamlit app
st.title("Welcome to Ashish's RAG ChatBot Powered by Google")

st.write("This chatbot is based on the content of a pre-loaded document.")

# Question input
question = st.text_input("Ask a question related to the document:")

if st.button("Get Answer"):
    # Use the entire document as context
    context = document_text

    # Generate answer using Google Generative AI
    answer = generate_answer(context, question)
    st.write(f"Answer: {answer}")
