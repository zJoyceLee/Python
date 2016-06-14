import pytesseract

from PIL import Image

image = Image.open('./captcha.jpg')

captcha = pytesseract.image_to_string(image)

print(captcha)
