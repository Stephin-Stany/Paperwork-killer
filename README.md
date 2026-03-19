# 📄 Paperwork Killer – Intelligent OCR Parser


Paperwork Killer is a project I built to extract structured data from messy documents like PDFs and images.

It uses OCR (Tesseract), image preprocessing (OpenCV), and a local LLM (Llama 3 via Ollama) to convert unstructured text into clean JSON output.

Features

- Supports PDF and image files
- Extracts text using Tesseract OCR
- Improves accuracy using OpenCV preprocessing
- Converts text into structured JSON using Llama 3
- Runs completely locally (no API needed)
- Simple web interface using Streamlit

How It Works

Document (PDF/Image)
↓
Convert PDF to images (pdf2image)
↓
Image preprocessing (OpenCV)
↓
Text extraction (Tesseract OCR)
↓
Structured extraction (Llama 3 via Ollama)
↓
JSON Output

Tech Stack

- Python
- Tesseract OCR
- OpenCV
- pdf2image + Poppler
- Ollama (Llama 3)
- Streamlit


 Setup

1. Install Python

2. Install dependencies
pip install -r requirements.txt

3. Install Tesseract OCR

4. Install Poppler and add to PATH

5. Run Ollama
ollama pull llama3
ollama serve


Run

Run backend:
python src/main.py

Run web app:
streamlit run app.py


Example Output

{
  "name": "John Doe",
  "passport_number": "A12345678",
  "date_of_birth": "01-01-1995",
  "country": "India"
}


What I Learned

- How OCR works using Tesseract
- Improving OCR accuracy using OpenCV
- Handling PDFs by converting them to images
- Using LLMs to extract structured data
- Building an end-to-end AI pipeline


Author

Stephin Stany