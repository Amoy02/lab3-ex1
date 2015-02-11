import smtplib
fromaddr = 'pattersonamoy@gmail.com'

toaddr = 'pattersonamoy@yahoo.com'

message = """From: {} <{}>

To: {} <{}>

Subject: {}

{}

"""
toname = 'Amoy'
fromname = 'Amoy'
msg = 'Hello'
subject = 'Greetings'
messagetosend = message.format(

 fromname,

 fromaddr,

 toname,

 toaddr,

 subject,

 msg)

# Credentials (if needed)

username = 'pattersonamoy@gmail.com'

password = 'vxayzzlfvjxsewhp'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()