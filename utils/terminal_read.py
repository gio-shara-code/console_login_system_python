from utils import validate
from utils import theme
from utils import console

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
        isValid = validate.email(email)
        if isValid == -1:
            console.warning("Incorrect email format.")
        else:
            return email
