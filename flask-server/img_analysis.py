import cv2
import pytesseract
import nltk
import re

nltk.download('punkt')
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def analyze_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    text = text.replace('|', 'I')

    lines = [line.strip() for line in text.split('\n') if line.strip()]

    def is_valid_line(line, idx):
        if idx < 4:
            if line.lower() in ["online", "today", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
                return False
        if re.search(r'\b\d{1,2}:\d{2}\s*[AP]M\b', line):
            return False
        return True

    lines = [line for idx, line in enumerate(lines) if is_valid_line(line, idx)]

    if lines and lines[-1].startswith("Type a message"):
        lines = lines[:-1]

    return lines
