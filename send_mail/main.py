import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Vlad Cristea'
email['to'] = ['cristeavladbmb@gmail.com']
email['subject'] = 'Mesaj test'


email.set_content(html.substitute({'name':'Mbappe','echipa':'Real Madrid'}), 'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('cristeavladbmb@gmail.com', 'hzzhitgfqkuvgqau')
    smtp.send_message(email)
    print('gata')


