import qrcode

# taking UPI id as a input
upi_id = input("Enter UPI id: ")

# Define various payment URl
phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# making QR code 
phonepe_Qr = qrcode.make(phonepe_url)
paytm_Qr = qrcode.make(paytm)
google_pay_Qr = qrcode.make(google_pay_url)

# Save Qr code
phonepe_Qr.save('phonepe_Qr.png')
paytm_Qr.save('paytm_Qr.png')
google_pay_Qr.save('google_pay_Qr.png')

# Display the Qr code 
phonepe_Qr.show()
paytm_Qr.show()
google_pay_Qr.show()

