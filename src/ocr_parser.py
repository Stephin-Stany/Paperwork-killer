import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import cv2
import numpy as np


def preprocess_image(pil_image):

    img = np.array(pil_image)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Increase contrast
    gray = cv2.convertScaleAbs(gray, alpha=1.5, beta=0)

    # Adaptive threshold
    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    return thresh


def extract_text(file_path):

    text = ""

    if file_path.lower().endswith(".pdf"):

        # Convert PDF pages → images
        images = convert_from_path(file_path, dpi=300)

        for img in images:

            processed = preprocess_image(img)

            text += pytesseract.image_to_string(processed, config="--psm 6")

    else:

        image = Image.open(file_path)

        processed = preprocess_image(image)

        text =pytesseract.image_to_string(processed, config="--psm 6")
    return text