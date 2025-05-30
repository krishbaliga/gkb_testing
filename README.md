# gkb_testing# 

This is a lightweight [Streamlit](https://streamlit.io) app that allows users to upload one or more image files and view their dimensions (width × height in pixels).

## 🚀 Features

- Upload multiple `.jpg`, `.jpeg`, or `.png` images
- Click a button to process the images
- Displays the dimensions of each uploaded image

## 📂 How to Use

1. Go to the deployed app: [https://your-app-name.streamlit.app](https://your-app-name.streamlit.app) *(replace with actual URL)*
2. Upload your image(s) using the file uploader
3. Click **"Show Image"**
4. See the dimensions listed below

## 🛠 Tech Stack

- Python
- Streamlit
- Pillow (PIL)

## 💻 Local Setup

```bash
# Clone the repo
git clone https://github.com/gb2219/gkb_testing.git
cd gkb_testing

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
