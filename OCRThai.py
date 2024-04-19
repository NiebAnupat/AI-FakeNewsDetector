from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def load_test_data():
    image_file = 'th-test.png'
    text = pytesseract.image_to_string(Image.open(
        image_file), lang='tha').replace(' ', '')
    return text

# create a function to convert image to string passing image file as parameter
def image_to_string(image_file) -> str:
    text = pytesseract.image_to_string(Image.open(
        image_file), lang='tha').replace(' ', '')
    return text
# test English text image to string
# print("English text image to string------------------")
# img = cv2.imread('en-test.jpg')
# print(pytesseract.image_to_string(img))
# print("------------------------------------------------")


# test Thai text image to string
# print("Thai text image to string------------------")
# image_file = 'th-test.png'
# print(pytesseract.image_to_string(Image.open(
#     image_file), lang='tha').replace(' ', ''))

# print("------------------------------------------------")
# image_file = 'th-test-2.png'
# text = pytesseract.image_to_string(Image.open(
#     image_file), lang='tha').replace(' ', '')
