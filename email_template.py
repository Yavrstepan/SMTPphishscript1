from pathlib  import *

class Email_template:
    '''This class is responsible for html templates,
    please create your own template for the script to work correctly'''


    def __init__(self, html_file = None, subject_file = None, file = None):
        if html_file is None and subject_file is None and file is None:
            self.content = "<h1>!!! CREATE YOUR TEMPALTE !!! </h1>"
            self.subject = "Create your own subject.txt"
            self.file = "Create docx file"

        else:
            self.html_file = Path(html_file)
            self.subject_file = Path(subject_file)
            self.file = Path(file)
            if self.html_file.exists():
                try:
                    with open(self.html_file, "r", encoding='utf-8') as f:
                        self.content = f.read() 

                except Exception as e:
                    print(f"Error reading the tempalte.html file: {e}")
                    raise

                
            if self.subject_file.exists():
                try:
                    with open(self.subject_file, "r", encoding='utf-8') as f:
                        self.subject = f.read().strip()
                except Exception as e:
                    print(f"Error reading subject.txt file: {e}")
                    raise

            if self.file.exists():
                try:
                    with open(self.file, "rb") as f:
                        self.file_content = f.read()
                    self.file_name = self.file.name
                except Exception as e:
                    print(f"Error reading file: {e}")
                    raise
    
        