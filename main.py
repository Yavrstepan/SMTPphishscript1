from email_parser import EmailParser
from email_template import Email_template
from email_sender import Smtp_sender
from security_manager import SecurityManager
from argparse import *
def parse_arguments():

    parser = ArgumentParser()
    
    group = parser.add_argument_group(title='Authentication options', description='authentication')
    group.add_argument('-l', '--login', required=True, help='Write your login')
    group.add_argument('-p', '--password', required=True, help='Write your password')
    group.add_argument('-s', '--smtpserver', required=True, help='Write your smtp server')
    group.add_argument('-f', '--From', required=True, help='Write a different sender name for phishing')

    return parser.parse_args()

def main():
    args = parse_arguments()
    try:
        send = Smtp_sender(args.login, args.password, args.smtpserver, args.From)
    except Exception as e:
        print(f"Failed to initialize SMTP sender: {e}")
        return
    
    confirm_path = input("\nYou have a directory that contains folders named email? (y/n) ")
    if confirm_path.lower() == "y":
        path_dir= input("Enter the path to the directory: ")
        parser = EmailParser(path_dir)
        correct_email=parser.parse_email()
    elif confirm_path.lower() == "n":
        print("The program will not work if you do not specify a folder")
        return
    else:
        print("Unknown command")
        return 
    
    confirm_template = input("\nDo you want to add your own HTML and subject markup to the email? (y/n) ")
    if confirm_template.lower() == "y":
        path_template = input("Enter the path to the template: ")
        path_subject = input("Enter the path to the subject.txt: ")
        template = Email_template(path_template, path_subject)
    elif confirm_template.lower() == "n":
        template = Email_template()
    else:
        print("Unknown command")
        return
    
    time_lim = input("Do you want emails to be sent in a specific range and have a specific limit that resets every hour? (y/n) ")
    if time_lim == "y":
        rate_limit = int(input("Message limit per hour: "))
        min_delay = int(input("Minimum delay in seconds: "))
        max_delay = int(input("Maximum delay in seconds: "))
        manager = SecurityManager(rate_limit, min_delay, max_delay)
    elif time_lim == "n":
        #Установим 100 сообщений в час по умолчанию, если не будет задержек
        manager = SecurityManager(100, 0, 0)
    else:
        print("Unknown command")
        return 
    
    try:
        for email in correct_email:
            if manager.can_send_message():
                manager.is_any_whitelisted(email)
                send.send_email(template, email)
                manager.time_tosend() 
    finally:
        send.close()

if __name__ == "__main__":
    main()

