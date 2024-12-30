import streamlit as st
import requests
import os
from dotenv import load_dotenv
from PIL import Image
import io

# Load environment variables
load_dotenv()

# Access API keys from .env file
HF_API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

# Extract keywords
def extract_keywords(caption: str) -> str:
    # Simple mock keyword extractor
    # Replace this with your own implementation as needed
    return caption

# Generate an image using the Hugging Face API
def generate_image(keywords: str) -> Image:
    payload = {"inputs": keywords}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return Image.open(io.BytesIO(response.content))
    else:
        st.error(f"Failed to generate image: {response.status_code}")
        st.error(f"Response: {response.text}")
        return None

# Streamlit UI
st.title("Text-to-Image Generator")
st.write("Enter a description, and we’ll generate an image for you!")

# User Input
caption = st.text_area("Enter your description:", placeholder="A scenic mountain view at sunset")
if st.button("Generate Image"):
    if not caption:
        st.warning("Please enter a description!")
    else:
        with st.spinner("Generating image..."):
            keywords = extract_keywords(caption)
            image = generate_image(keywords)
            if image:
                st.image(image, caption="Generated Image", use_column_width=True)
