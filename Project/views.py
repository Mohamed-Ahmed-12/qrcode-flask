from flask import Blueprint, render_template, redirect, url_for, request
import base64
import qrcode
from io import BytesIO

# Create a blueprint
api = Blueprint('api', __name__)


@api.route('/qrcode',methods=['GET','POST'])
def qrcode_generation():
  if request.method == 'POST':
    userInput = request.form['link']
    qr = generate_qr(userInput)
    return render_template('scan.html', img_base64  = qr)
  
  return render_template('scan.html')



# Generate a new QR code with the updated link
def generate_qr(link):
  print(link)
  qr_code_img = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )
  qr_code_img.add_data(link)
  qr_code_img.make(fit=True)

  # Create an image for the QR code
  img = qr_code_img.make_image(fill_color="black", back_color="white")

  # Save the image in memory using BytesIO
  buffer = BytesIO()
  img.save(buffer)
  buffer.seek(0)
  img_data = buffer.read()
  # Pass the image data to the template as base64 encoded image
  img_base64 = base64.b64encode(img_data).decode('utf-8')

  return img_base64
