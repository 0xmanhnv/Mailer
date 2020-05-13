import smtplib, ssl

port = 465
sender = 'sender@gmail.com' #sender's address
password = 'pwd' #password
recieve = ['recievermail@something.com'] #reciver's mail
msg = """\
Subject: Python Mail 
This is an email from python, wassup??
"""
context = ssl.create_default_context()

print("Starting to send")
with smtplib.SMTP_SSL("smtp.gmail.com",port, context=context ) as server:
    server.login(sender, password)
    server.sendmail(sender, recieve, msg)
print("sent")