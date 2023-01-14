import smtplib
from email.mime.text import MIMEText
# from email.mime.base import MIMEBase

gmail_user = 'parker178912@gmail.com' # your gmail account
gmail_password = 'cookie36978' # your gmail password


msg = MIMEText('This is test email for automation.')
msg['Subject'] = 'Automation Test from GCP'
msg['From'] = gmail_user
msg['To'] = 'parker178912@gmail.com'


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo() #The EHLO command tells the receiving server it supports extensions compatible with ESMTP
server.login(gmail_user, gmail_password)
server.send_message(msg)
server.quit()
