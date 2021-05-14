from utils import validate
from utils import theme
from utils import console
from enums.answer import Answer
from enums.email import Email

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
        if validate.email(email) == Email.NOT_CORRECT_FORMAT:
            console.warning("Incorrect email format, please try again.")
        else:
            return email

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