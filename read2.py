from PIL import Image
from pyzbar.pyzbar import decode
data = decode(Image.open('qr.png'))
print(data)
