import smtplib
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
SUBJECT = "Interview Call"
s = smtplib.SMTP('smtp.gmail.com', 587)

# def sendmail(TEXT,email):
#     print("sorry we cant process your candidature")
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.starttls()
#     s.login("il.pradeepthi@gmail.com", "oms@1Ram")
#     message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
#     s.sendmail("il.pradeepthi@gmail.com", email, message)
#     s.quit()
# def sendgridmail(user,TEXT):
user = 'viranthrocky@gmail.com'
TEXT = 'HELLO WELCOME'
sg = sendgrid.SendGridAPIClient('API-KEY')
from_email = Email("1915025@nec.edu.in")  # Change to your verified sender
to_email = To(user)  # Change to your recipient
subject = "Sending with SendGrid is Fun"
content = Content("text/plain",TEXT)
mail = Mail(from_email, to_email, subject, content)
response = sg.send(mail)
print(response.status_code)
print(response.body)
print(response.headers)

# Get a JSON-ready representation of the Mail object
# Send an HTTP POST request to /mail/send
#response = sg.client.mail.send.post(request_body=mail_json)
#print(response.status_code)
#print(response.headers)
    

#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