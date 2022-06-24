import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "http://aayush-portfolio.s3-website.ap-south-1.amazonaws.com/"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("aayush-portfolio.svg", scale = 8) 