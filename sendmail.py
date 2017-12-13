import smtplib

senders = 'kboysreel@gmail.com'  
password = '19sedimat54!'
recievers = 'kboysred@yahoo.com!'

# try:  
#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server.ehlo()
#     server.login(gmail_user, gmail_password)
# except:  
#     print ('Something went wrong...')

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com', 465)
   smtpObj.login(senders, password)
   smtpObj.sendmail(senders, recievers, message)         
   print ("Successfully sent email")
except:
   print ("Error: unable to send email")