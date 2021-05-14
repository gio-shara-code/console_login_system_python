from enums.answer import Answer
from utils import console
from utils import theme
from services import user_services
from utils import terminal_read

def login():
    while True:
        email = terminal_read.email()
        user = user_services.get_user_by_email(email)
        if(user == -1):
            console.statement(f'{email} does not exists. Please try again.')
        else:
            console.statement(f'Welcome {user["firstName"]} {user["lastName"]}!')
            return
        
        answer = terminal_read.yes_no()
        if answer == Answer.YES:
            continue
        return
        
        

def register():
    pass
    


