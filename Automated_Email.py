import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "expolozo2016@gmail.com"
toaddr = "salmanakbana@gmail.com"
password = "EMAILMAILINGSERVICEFORSCHEDULEOFCLASSES123"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Automated Email"

body = "Do not reply to this email. This is a test email"
msg.attach(MIMEText(body, 'plain'))

filename = "NAME OF THE FILE WITH ITS EXTENSION"
attachment = open("PATH OF THE FILE", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachement; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


