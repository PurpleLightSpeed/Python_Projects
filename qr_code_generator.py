import qrcode

data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename (with .png extension): ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)  # Make the QR code before creating the image
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR code saved as {filename}")


# In Terminal: source venv/bin/activate
# Run: python qr_code_generator.py