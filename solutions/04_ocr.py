from urllib.request import urlopen
from gazpacho import get, Soup
from PIL import Image # pip install pillow
import pytesseract # pip install pytesseract

base = 'http://localhost:5000'
url = base + '/ocr'
html = get(url)
soup = Soup(html)

soup.find("img")

imgs = soup.find('img')
paths = [i.attrs['src'] for i in imgs]

images = []
for path in paths:
    url = base + path
    im = Image.open(urlopen(url))
    images.append(im)

text = ''
for image in images:
    i2t = pytesseract.image_to_string(image)
    text += i2t

print(text)
