import pyqrcode

url = input("enter url to generate qr code: ")

qr_code = pyqrcode.create(url)
qr_code.svg("qrcode.svg", 5)
