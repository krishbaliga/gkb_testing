import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.title("Image API Test with Simulated Edits")

grayscale = st.checkbox("Apply Grayscale Filter")

uploaded_files = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if st.button("Show Image"):
    if uploaded_files:
        for file in uploaded_files:
            image = Image.open(file)
            width, height = image.size
            st.image(image, caption=f"Original: {file.name} - Size: {width}x{height}")

            url = f"https://picsum.photos/{width}/{height}"
            if grayscale:
                url += "?grayscale"
                
            response = requests.get(url)
            if response.status_code == 200:
                edited_image = Image.open(BytesIO(response.content))
                st.image(edited_image, caption=f"Edited (simulated) for {file.name}")
            else:
                st.error(f"API failed for {file.name} (status {response.status_code})")
    else:
        st.warning("No Files Uploaded")
