import smtplib
SUBJECT = 'please complete the assignment'
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('virathrocky@gmail.com', 'qzxmscsjzmvhjccu')
message  = 'Subject: {}\n\n{}'.format(SUBJECT, 'just prank you')
s.sendmail('virathrocky@gmail.com', 'sathiesramya1313@gmail.com', message)

# qzxmscsjzmvhjccu
