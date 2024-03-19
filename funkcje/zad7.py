import smtplib
import ssl
 
mailFrom = 'maciejbujalski9@gmail.com'
mailTo = ['maciej.bujalski12@interia.pl']
mailSubject = 'Processing finished successfully'
mailBody = '''Hello
 
This mail confirms that processing has finished without problems,
 
Have a nice day!'''
 
message = '''From: {}
Subject: {}
 
{}
'''.format(mailFrom, mailSubject, mailBody)
 
user = 'maciejbujalski9@gmail.com'
password = 'xkbxlwluecohukbj'
 
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('error sending email')