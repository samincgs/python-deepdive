import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.environ.get('GMAIL_EMAIL')


# email_smtp = smtplib.SMTP('smtp.gmail.com', 587)
# email_smtp.ehlo()

# email_smtp.close()