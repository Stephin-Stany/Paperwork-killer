from ocr_parser import extract_text
from llm_extractor import extract_json

text = extract_text("input_files/ocr_test_document.pdf")

print("OCR TEXT:")
print(text)

json_output = extract_json(text)

print("\nStructured JSON:")
print(json_output)