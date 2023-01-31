import smtplib
import ssl
import os
# I have created a random Gmail account for this experiment
# This is not my daily use Gmail address
def sendEmail(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'dnero543@gmail.com'
    password = os.getenv('password')
    receive = 'dnero543@gmail.com'
    context = ssl.create_default_context()



    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receive, message)