from pathlib  import *
import re


class EmailParser:
    '''This class parses folders whose names are email addresses'''
    
    def __init__(self, papka):
        self.papka=Path(papka)
        self.allemail_list = []
        self.correct_email = []
        self.novalid_email = []

    def parse_email(self):
        regex = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}'

        if not self.papka.exists(): 
            print(f"Your folder {self.papka} does not exist, or you have copied the path incorrectly")
            return 
        
         # проверим, а является ли обьект директорией в указанной папке
        for path in self.papka.iterdir():
            if path.is_dir():
                self.allemail_list.append(path.name)
            else:
                print(f"This path is not a folder '{path}'")

        for email_name in self.allemail_list:
            if re.fullmatch(regex, email_name):
                self.correct_email.append(email_name)
            else:
                self.novalid_email.append(email_name)
                print(f"This '{email_name}' email does not exist")
                
        print(f"total number of correct addresses {len(self.correct_email)}")
        return self.correct_email

    def get_valid_email(self):
        with open('invalid_emails.txt', 'w', encoding='utf-8') as file:
            for notcorrext_email in self.novalid_email:
                file.write(f"non-existent email: {notcorrext_email}")
        



