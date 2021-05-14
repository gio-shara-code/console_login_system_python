from utils import validate
from utils import theme
from utils import console
from enums.answer import Answer
from enums.email import Email
from enums.input import Input

def option():    
    while True:
        try:
            option = int(input(theme.input("Option: ")))
            if option <1 or option > 2:
                console.warning("Wrong option, try again")
                continue
            return option
        except:
            console.warning("Wrong option, try again")
    
def email():
    while True:
        email = input(theme.input("Email: "))
        if validate.email(email) == Input.NOT_CORRECT_FORMAT:
            console.warning("Incorrect email format, please try again.")
        else:
            return email

def name():
    while True:
        name = input(theme.input("Name (e.g. Robert Schulz): "))
        if validate.name(name) == Input.NOT_CORRECT_FORMAT:
            console.warning("Incorrect name. Name should only contain chachters.")
        else:
            return name

def password():
    while True:
        pwd = input(theme.input("Password (min. 4 and max. 8 characters): "))
        if validate.password(pwd) == Input.NOT_CORRECT_FORMAT:
            console.warning("Password length should be min. 4 and max. 8 characters only charachters")
        else:
            return pwd

def yes_no():
    while True:
        answer = input(theme.yellow_bold("Do you want to try again? (y/n): "))
        if answer.lower() == "n":
            console.statement("See you.")
            return Answer.NO
        elif answer.lower() == "y":
            return Answer.YES
        else:
            console.statement(f"{answer} is not a proper answer, please try again")