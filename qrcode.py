'''import qrcode
image=qrcode.make("https://docs.google.com/document/d/13pe902DuM5XlTNYZGCVr8VNXO2k8twSaDhlxZPpkKBQ/mobilebasic")
image.save("neha.png")
print("successfuly installed")'''

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")

img.save("new.png")