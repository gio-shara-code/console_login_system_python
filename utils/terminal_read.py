from utils import validate
from utils import theme
from utils import console

# def option():    
#         option_is_invalid = True
#         while option_is_invalid:
#             try:
#                 option = int()
#                 option_is_invalid = False
#                 return option
#             except:
#                 return -1
    
def email():
    is_email_not_valid = True
    while is_email_not_valid:
        email = input(theme.input("Email: "))
        isValid = validate.email(email)
        if isValid == -1:
            console.warning("Incorrect email format.")
        else:
            return email

