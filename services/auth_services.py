from enums.answer import Answer
from utils import console
from utils import theme
from services import user_services
from utils import terminal_read
from enums.email import Email

def login():
    while True:
        email = terminal_read.email()
        user = user_services.get_user_by_email(email)
        if(user == Email.DOES_NOT_EXIST):
            console.statement(f'{email} does not exists. Please try again.')
        else:
            console.statement(f'Welcome {user["firstName"]} {user["lastName"]}!')
            return
        
        answer = terminal_read.yes_no()
        if answer == Answer.NO:
            return
        
        

def register():
    pass
    


