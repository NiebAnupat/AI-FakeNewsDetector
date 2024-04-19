from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def load_test_data():
    image_file = 'th-test.png'
    text = pytesseract.image_to_string(Image.open(
        image_file), lang='tha').replace(' ', '')
    return text

def image_to_string(image_file) -> str:
    text = pytesseract.image_to_string(Image.open(
        image_file), lang='tha').replace(' ', '')
    return text
