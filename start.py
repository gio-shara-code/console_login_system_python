import re
from utils.print import Print
from utils.input import Input
from services import user_services



def login():
    Print.headline("login")
    is_user_not_logged_in = True
    while is_user_not_logged_in:

        is_email_not_valid = True
        email = ""
        while is_email_not_valid:
            email = input("Please input your email: ")
            email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
            if re.search(email_regex, email):
                is_email_not_valid = False
            else:
                print(f'Format incorrect for: {email}')

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



    

Print.headline("welcome")
Print.options()

option = Input.option()

if option == 1:
    login()
elif option == 2:
    print("Register")
elif option == -1:
    print(f"Option not valid")
else:
    print(f'The option {option} doesn\'t exist')

    
# existing email => krish.lee@learningcontainer.com
# non-existing email => non.existing@email.com

