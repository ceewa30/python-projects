from email.message import EmailMessage
import smtplib
import ssl

email_sender = 'ceewa30@gmail.com'
email_password = 'lphxoimlvsuwhynz'

# https://temp-mail.org/
email_reciver = 'fimeyi4106@stikezz.com'

subject = 'Dont forget to subscribe'
body = 'Hey, please add me to your subscribers list. I promise to send you great content!'

em = EmailMessage()
em['From'] =  email_sender
em['To'] = email_reciver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smpt:
    smpt.login(email_sender, email_password)
    smpt.sendmail(email_sender, email_reciver, em.as_string())