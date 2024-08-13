import streamlit as st
import google.generativeai as palm

# Configure the API key for Google Generative AI
api_key = 'AIzaSyCmM4R1UOC6Hy9_CyG0EsL1ZxddX5x9z-4'
palm.configure(api_key=api_key)

def generate_response(prompt, model):
    """
    Generates a text response from the Google Generative AI model based on the provided prompt.

    Parameters:
        prompt (str): The input text for the model to respond to.
        model (str): The name of the model to use.

    Returns:
        str: The generated text from the model.
    """
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,  # Fixed temperature
        max_output_tokens=800,  # Fixed max output tokens
    )
    return completion.result

# Streamlit app
st.title("Welcome to Ashish's ChatBot Powered by Google")

# Model selection
model = "models/text-bison-001"

# User input
prompt = st.text_area("Enter your prompt here:")

# Generate response
if st.button("Generate Response"):
    if prompt.strip():
        with st.spinner("Generating response..."):
            response = generate_response(prompt, model)
        st.subheader("Response:")
        st.write(response)
    else:
        st.error("Please enter a prompt.")

# Footer
st.markdown("Developed by Ashish.")
