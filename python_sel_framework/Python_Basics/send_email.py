import smtplib
import os.path as op
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# message to be sent   
emailbody=""" Hi,\n

Message sent from SMTP python email program\n

Thanks,
Raghu

"""
msg = 'Subject: {}\n\n{}'.format("Test python email", emailbody)

recipients = ['raghurajuchekuri@gmail.com']
#recipients = ['raghurajuchekuri@gmail.com', 'smadan8292@gmail.com','cc.malati@gmail.com' ]


# open the file to be sent  
filename = "File_name_with_extension"
attachment = open("text.txt", "rb") 
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream')
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
# encode into base64 
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
text = msg.as_string() 

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #Next, log in to the server
    server.login("framework.reports@gmail.com", "pyThon#19")    
    server.sendmail("framework.reports@gmail.com", recipients, text)       
    #smadan8292@gmail.com,cc.malati@gmail.com
    server.close()
    print ('successfully sent the mail')
except:
    print ("failed to send mail")



