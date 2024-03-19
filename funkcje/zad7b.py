import smtplib
import ssl
import functools

def SendInfoEmail(user,password,mailFrom,mailTo,mailSubject,mailBody):

    message = '''From: {}
Subject: {}
 
{}
'''.format(mailFrom, mailSubject, mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('mail sent')
    except:
        print('error sending email')


mailFrom = 'maciejbujalski9@gmail.com'
mailTo = ['maciej.bujalski12@interia.pl']
mailSubject = 'Processing finished successfully'
mailBody = '''Hello Agatka
 
Kocham Cie,
 
Have a nice day!'''



user = 'maciejbujalski9@gmail.com'
password = 'xkbxlwluecohukbj'



SendInfoEmailFromGmail = functools.partial(SendInfoEmail, user, password)

SendInfoEmailFromGmail(mailFrom, mailTo, mailSubject, mailBody)
