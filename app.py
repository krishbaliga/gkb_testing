import streamlit as st
from PIL import Image

uploaded_files = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
if st.button("Show Image"):
    if uploaded_files:
        for file in uploaded_files:
            def process_images(img):
                return img.size
            image = Image.open(file)
            size = process_images(image)
            st.image(image, caption=f"{file.name} - Size: {size}")
    else:
        st.warning("No Files Uploaded")
