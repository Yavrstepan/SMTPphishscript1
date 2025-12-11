SMTPphishscript1
🔐 SMTP phishing simulator for authorized penetration testing & security awareness training. Educational purposes only. Use responsibly with proper authorization.

So, on this GitHub account, I will be taking my first steps into the world of pentesting. Although I have some knowledge in the IT field, this is my first encounter with cybersecurity. As this is a new and unfamiliar area for me, I have quickly become interested in it.

Let's imagine that we have a customer who wants to test the critical thinking or vigilance of their employees and asks the order executor to send fake emails (containing malicious scripts, for example) on behalf of the Boss. In the company where I'm interning, I was asked to write a small program that would send these emails because it would take too long to do it manually.

To implement this task, I chose the Python programming language and its built-in libraries:

pathlib — for working with file paths
smtplib — for sending emails
argparse — for handling command-line arguments
re — for regular expressions
MimeMultipart and MIMEText — for creating emails with attachments
datetime — for working with dates and times
time — for the delay between sending emails
My script consists of 4 classes:

EmailParser
SecurityManager
Email_template
Smtp_sender
EmailParser -
