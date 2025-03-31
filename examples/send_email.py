import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.environ.get('GMAIL_EMAIL')
EMAIL_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')

# send an email
img_file = open('modules/pillow/soul.jpg', 'rb')

img_data = img_file.read()
img_type = img_file.name.split('.')[-1]
img_name = img_file.name.split('/')[-1]

img_file.close()


# send a pdf
# pdf_file = open('.....', 'rb')
# pdf_data = pdf_file.read()
# pdf_file.close()

# msg.add_attachment(pdf_data, maintype='application', subtype='octet-stream', filename=pdf_name)




msg = EmailMessage()

msg['Subject'] = 'Check out my new profile picture!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('Image attached...')
msg.add_attachment(img_data, maintype='image', subtype=img_type, filename=img_name)

with smtplib.SMTP('smtp.gmail.com', 587) as email_smtp:
    email_smtp.starttls()
    email_smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    email_smtp.send_message(msg)


