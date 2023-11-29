import smtplib
import imghdr
from email.message import EmailMessage
from emaillAccess import  _get_email_key

get_email = _get_email_key()
email_key = ('sender', 'password', 'receiver')

result = {email_key[i] : get_email[i]  for i, _ in enumerate(email_key)}


SENDER = result['sender']
PASSWORD = result['password']
RECEIVER = result['receiver']

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new Customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/24.png")

