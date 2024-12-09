import qrcode

qr=qrcode.make("") ##In this space write what you want to QR code

qr.save("my_qrcode.png")
print("QR code generated and saved as png")