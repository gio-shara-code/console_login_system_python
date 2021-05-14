import re
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
        email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if re.search(email_regex, email):
            is_email_not_valid = False
            return email
        else:
            print(f'Format incorrect for: {email}')