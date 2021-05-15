from services import auth_services
from utils import console
from utils import terminal_read
from enums.option import Option

console.headline("welcome")
console.options()

option = terminal_read.option()

if option == Option.LOGIN.value:
    console.headline("login")
    auth_services.login()

elif option == Option.REGISTER.value:
    console.headline("register")
    auth_services.register()

elif option == Option.FORGOT_PASSWORD.value:
    console.headline("forgot password")
    auth_services.forgot_password()

else:
    console.warning(f'Option doesn\'t exist')
 
# existing email => krish.lee@learningcontainer.com
# non-existing email => non.existing@email.com
