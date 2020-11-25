from PIL import Image
import qrcode

url = 'https://github.com/monish-mnjds'
file_format = 'High_courts_of_India.png'
img = qrcode.make(url)
img.save(file_format)
im = Image.open(file_format)
im.show()
