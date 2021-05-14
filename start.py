from utils.print import Print
from utils.input import Input
from services import auth_services


Print.headline("welcome")
Print.options()

option = Input.option()

if option == 1:
    auth_services.login()
elif option == 2:
    print("Register")
elif option == -1:
    print(f"Option not valid")
else:
    print(f'The option {option} doesn\'t exist')

    
# existing email => krish.lee@learningcontainer.com
# non-existing email => non.existing@email.com

