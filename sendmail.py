from email.mime.application import MIMEApplication
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename

mail_content = '''Helloo this an amazing mail. I hope you are enjoying this mail. Thank you'''

sender_address = '20z208@psgtech.ac.in'
sender_pass = 'ASHWIN12345'
receiver_address = '20z208@psgtech.ac.in'

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Boohoo'  

message.attach(MIMEText(mail_content, 'plain'))
# f='read.py'
# with open(f, "rb") as fil:
#         part = MIMEApplication(fil.read(),Name=basename(f))
#         part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
#         message.attach(part)

session = smtplib.SMTP('smtp.gmail.com', 587) 
session.starttls() 
session.login(sender_address, sender_pass) 
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')