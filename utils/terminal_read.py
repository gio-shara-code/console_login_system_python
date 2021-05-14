from utils import validate

def option():    
        option_is_invalid = True
        while option_is_invalid:
            try:
                option = int(input("Please input your option: "))
                option_is_invalid = False
                return option
            except:
                return -1
    
def email():
    is_email_not_valid = True
    while is_email_not_valid:
        email = input("Please input your email: ")
        isValid = validate.email(email)
        if isValid == -1:
            print(f'Format incorrect for: {email}')
        else:
            return email
