from utils import console
from utils import terminal_read
from services import auth_services


console.headline("welcome")
console.options()

option = terminal_read.option()

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

