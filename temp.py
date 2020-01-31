from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from wand.image import Image as Img
from wand.display import display
import nltk
from nltk.tokensize import word_tokensize
from nltk.tag import pos_tag
import numpy as np






im = Image.open(r"C:\Users\Dory\Desktop\OCR test\ocr.png")

text = pytesseract.image_to_string(im, lang = 'eng')


saveFile = open('savedOutput.txt','w')
saveFile.write(text)
saveFile.close()

print(text)