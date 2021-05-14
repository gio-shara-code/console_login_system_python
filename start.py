from services import auth_services
from utils import console
from utils import theme
from utils import terminal_read

console.headline("welcome")
console.options()

option = terminal_read.option()

if option == 1:
    console.headline("login")
    auth_services.login()
elif option == 2:
    console.headline("register")
    auth_services.register()
else:
    console.warning(f'Option doesn\'t exist')
    
# existing email => krish.lee@learningcontainer.com
# non-existing email => non.existing@email.com

