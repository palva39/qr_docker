import qrcode

def generate_qr_code():
    url = "https://github.com/palva39"  # Replace with your GitHub URL
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("/app/qr_code.png")  # Save in the container

if __name__ == "__main__":
    generate_qr_code()
