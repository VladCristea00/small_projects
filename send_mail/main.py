import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Vlad Cristea'
email['to'] = ['mail.com']
email['subject'] = 'Mesaj test'


email.set_content(html.substitute({'name':'Mbappe','echipa':'Real Madrid'}), 'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('yourmail@gmail.com', 'pass')
    smtp.send_message(email)
    print('gata')


