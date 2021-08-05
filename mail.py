import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = input("Your email address:")
password = input("Your password:")
send_to_email = input("Send the email to:")
subject = input("Your Subject:")
message = input("Your message:")

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject


msg.attach(MIMEText(message, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
print("The email was sent successfully")
