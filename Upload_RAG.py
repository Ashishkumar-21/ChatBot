import streamlit as st
import PyPDF2
import google.generativeai as palm

# Configure the API key for Google Generative AI
api_key = 'AIzaSyCmM4R1UOC6Hy9_CyG0EsL1ZxddX5x9z-4'
palm.configure(api_key=api_key)

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

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

uploaded_file = st.file_uploader("Upload a PDF or Text File", type=["pdf", "txt"])

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        document_text = extract_text_from_pdf(uploaded_file)
    else:
        document_text = uploaded_file.getvalue().decode("utf-8")

    st.write("Document uploaded and processed.")

    # Question input
    question = st.text_input("Ask a question related to the document:")

    if st.button("Get Answer"):
        # Retrieve the entire document or relevant parts (for simplicity, using the whole document here)
        context = document_text  # In a more sophisticated setup, you would retrieve only relevant parts

        # Generate answer using Google Generative AI
        answer = generate_answer(context, question)
        st.write(f"Answer: {answer}")
