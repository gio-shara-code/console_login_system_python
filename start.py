import json
import re

f = open("users.json")
users = json.load(f)["users"]

def get_user_by_email(email_address: str):
    for user in users:
        if(user["emailAddress"] == email_address):
            return user
    return -1

def login():
    print_headline("login")
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

        user = get_user_by_email(email)
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




    



def input_option():
    option_is_invalid = True
    while option_is_invalid:
        try:
            option = int(input("Please input your option: "))
            option_is_invalid = False
            return option
        except:
            print(f'{option} is not an appropriate option')



class Print:

    @staticmethod
    def print_options(age):
        print(" 1. Login")
        print(" 2. Register\n")

    @staticmethod
    def print_headline(headline: str):
        print(f"\n### {headline.upper()} ###")


Print.print_headline("welcome")
Print.print_options()

option = input_option()

if option == 1:
    login()
else:
    print(f'The option {option} doesn\'t exist')

    

# existing email => krish.lee@learningcontainer.com
# non-existing email => non.existing@email.com

