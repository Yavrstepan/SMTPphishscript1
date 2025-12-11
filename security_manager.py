import time
import random 
from datetime import datetime

class SecurityManager:
    '''This class contains the logic that allows
       the recipient server not to block us for spam,
       if there are emails to which emails should not be sent,
       create a white_list.txt file and write these addresses'''



    def __init__(self, rate_limit, min_delay, max_delay):
        # Валидация
        if min_delay < 0 or max_delay < 0:
            raise ValueError("Delays cannot be negative")
        if min_delay > max_delay:
            raise ValueError("The minimum delay cannot be greater than the maximum")
        if rate_limit <= 0:
            raise ValueError("The sending limit must be a positive number.")
        
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.rate_limit = rate_limit
        self.current_hour = datetime.now().hour  
        self.sent_count = 0

        try:
            with open("white_list.txt", "r") as file:
                self.whitelist = {line.strip().lower() for line in file if line.strip()}

        except FileNotFoundError:
            print("The white_list.txt file was not found. An empty white list was created.")
            self.whitelist = set()
            

    def is_any_whitelisted(self, email):
        # email атрибут который будет получен в ходе работы функции main
        
        if email.lower() in self.whitelist: 
            print(f"addresses that are contained in white_list.txt '{email}'")
        return False
        
    def can_send_message(self):
        #rate_limit это сколько мы можем письм отправлять, если час прошел, то rate_limit обнуляется 
        now = datetime.now()
        if now.hour != self.current_hour:  
            self.current_hour = now.hour
            self.sent_count = 0  

        if self.sent_count < self.rate_limit:
            self.sent_count += 1
            print(f"Sent emails count: {self.sent_count}")
            return True
        
        return False

    def time_tosend(self):
        time.sleep(random.uniform(self.min_delay, self.max_delay))
        