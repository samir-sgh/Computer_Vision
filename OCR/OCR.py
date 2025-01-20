from PIL import Image
import pytesseract

# Specify the Tesseract OCR executable path
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

# Open an image file
image = Image.open('image.png')

# Use Pytesseract to convert the image to text
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)