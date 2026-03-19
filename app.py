import streamlit as st
import tempfile
from src.ocr_parser import extract_text
from src.llm_extractor import extract_json

st.title("📄 Paperwork Killer")
st.write("Upload a document and extract structured data")

uploaded_file = st.file_uploader(
    "Upload PDF or Image",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix="." + uploaded_file.name.split(".")[-1]
    ) as tmp:

        tmp.write(uploaded_file.read())
        file_path = tmp.name

    st.write("Processing document...")


    # OCR
    text = extract_text(file_path)

    # LLM extraction
    result = extract_json(text)

    st.subheader("Extracted Structured Data")

    st.code(result, language="json")