import smtplib

from email.mime.text import MIMEText
from email.header import Header

message = MIMEText('メールの本文を記載する')
message['Subject'] = Header('メールの件名を記載する', 'utf-8')
message['From'] = '17fi084@gmail.com'
message['To'] = '17fi084@ms.dendai.ac.jp'

with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
    smtp.login('17fi084', 'gathufreqyblicbd')
    smtp.send_message(message)
