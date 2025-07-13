import qrcode
linkedin_url = "https://www.linkedin.com/in/jakku-madhu-575514218"
qr = qrcode.make(linkedin_url)
qr.save("linkedin_qr.png")
print("✅ QR code for your LinkedIn profile has been saved as linkedin_qr.png")





















# import qrcode
# qr=qrcode.make("Follow @Pycode.Hubb!")
# qr.save("my_qr.png")
# print("QR code generated and saved as my_qr.png")