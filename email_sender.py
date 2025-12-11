import smtplib            
from email.mime.text import MIMEText         
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
class Smtp_sender:
    '''This class is responsible for the logic of sending mail.'''


    def __init__(self, emlogin, password, smtpserver, fromemail):
        try:
            self.mtpObj = smtplib.SMTP(smtpserver, 587)
            self.mtpObj.starttls()
            self.emlogin = emlogin
            self.password = password
            self.fromemail = fromemail
            self.mtpObj.login(emlogin, password)
            print("Successful connection!!!")

        except smtplib.SMTPAuthenticationError as e:
            print(f"Authentication error {e}")
            raise

        except smtplib.SMTPConnectError as e:
            print(f"Check your SMTP server connection {e}")
            raise

        except smtplib.SMTPException as e:
            print(f"SMTP error occurred: {e}")
            raise

        except Exception as e:
            print(f"Unexpected error: {e}")
            raise   
        
    
    def send_email(self, template, email):
        #email это список который мы получим из экземпляра класса EmailParser, а появился тут из-за передачи аргумента в цикле в main 

        try:
            msg = MIMEMultipart()
            msg['Subject'] = template.subject
            msg['From'] = self.fromemail
            msg['To']=email
            msg.attach(MIMEText(template.content, "html"))
            
            if hasattr(template, 'file_content') and template.file_content:
                attach = MIMEApplication(
                    template.file_content, 
                    _subtype="vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
                attach.add_header(
                    'Content-Disposition',
                    'attachment',
                    filename=template.file_name
                )
                msg.attach(attach)
            else:
                msg.attach(MIMEText(template.file, "html"))
            
            self.mtpObj.send_message(msg)
            print(f"{email} email sent successfully")

        except Exception as e:
            print(f"Email {email} not sent. Error: {e}")
            
    def close(self):
        self.mtpObj.quit()