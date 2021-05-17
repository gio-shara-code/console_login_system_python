from services import auth_services
from utils import console_log
from utils import terminal_read
from enums.option import Option

console_log.headline("welcome")
console_log.options()

option = terminal_read.option()

if option == Option.LOGIN.value:
    console_log.headline("login")
    auth_services.login()

elif option == Option.REGISTER.value:
    console_log.headline("register")
    auth_services.register()

elif option == Option.FORGOT_PASSWORD.value:
    console_log.headline("forgot password")
    auth_services.forgot_password()

elif option == Option.RESET_PASSWORD.value:
    console_log.headline("reset password")
    auth_services.reset_password()

else:
    console_log.warning(f'Option doesn\'t exist')
