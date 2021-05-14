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

        willing_not_continue = True
        while willing_not_continue:
            answer = input(theme.yellow_bold("Do you want to try again? (y/n): "))
            if answer.lower() == "n":
                console.statement("See you.")
                return
            elif answer.lower() == "y":
                willing_not_continue = False
            else:
                console.statement(f"{answer} is not a proper answer")

def register():
    pass
    


