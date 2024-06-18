import qrcode
import os

def generate_qr(data, filename):
    # Ensure the directory exists
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR Code generated and saved as {filename}")

# Get data and filename from user
data = input("Enter the data to encode in the QR code: ")
filename = input(r"Enter the filename to save the QR code image (e.g., 'D:\Internships\Audit+\Students attendance\Using QR\QRUser123.png'): ")

# Generate QR code
generate_qr(data, filename)
