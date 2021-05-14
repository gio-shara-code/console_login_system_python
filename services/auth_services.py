import re
from utils import console
from services import user_services

def login():
    console.headline("login")
    is_user_not_logged_in = True
    while is_user_not_logged_in:

        
        email = email()
        user = user_services.get_user_by_email(email)
        if(user == -1):
            print(f'{email} does not exists.')
        else:
            print(f'Welcome {user["firstName"]} {user["lastName"]}!')
            is_user_not_logged_in = True
            break

        willing_not_continue = True
        while willing_not_continue:
            answer = input("Do you want to try again? (y/n): ")
            if answer.lower() == "n":
                print("See you!")
                return
            elif answer.lower() == "y":
                willing_not_continue = False
            else:
                print(f'{answer} is not a proper answer')


def register():
    pass

def email():
    email = ""
    is_email_not_valid = True
    while is_email_not_valid:
        email = input("Please input your email: ")
        email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if re.search(email_regex, email):
            is_email_not_valid = False
        else:
            print(f'Format incorrect for: {email}')
