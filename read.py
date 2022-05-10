from qrtools import qrtools

from qrtools import qrtools
from PIL import Image
import zbarlight

qr = qrtools.QR()

#from qrtools import QR
my_QR = QR(filename = "qr.png")

# decodes the QR code and returns True if successful
my_QR.decode()

# prints the data
print (my_QR.data)
