from pyzbar.pyzbar import decode
from PIL import Image
decodeQR = decode(Image.open("QR.png"))
print(decodeQR[0].data.decode('ascii'))