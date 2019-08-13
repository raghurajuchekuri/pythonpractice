# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 


fromaddr = "framework.reports@gmail.com"
#toaddr = ['raghurajuchekuri@gmail.com', 'smadan8292@gmail.com','cc.malati@gmail.com']
toaddr = 'raghurajuchekuri@gmail.com'

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = fromaddr 
# storing the receivers email address 
#msg['To'] = toaddr
# storing the subject 
msg['Subject'] = "Python Automation Test Report"
# string to store the body of the mail 
body = """ Hi,\n
The python test reports are attached\n
Thanks,
Raghu
"""
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
# open the file to be sent 
filename = "text.txt"
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

try: 
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    # start TLS for security 
    s.starttls() 
    # Authentication 
    s.login(fromaddr, "pyThon#19") 
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    # terminating the session 
    s.quit() 
    print ('successfully sent the mail')
except smtplib.SMTPException as e:
    print('SMTP error occurred: ' + str(e))
except:
    print ("failed to send mail")