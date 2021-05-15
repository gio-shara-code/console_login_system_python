from enums.answer import Answer
from utils import console
from services import user_services
from utils import terminal_read
from enums.email import Email


def login():
    while True:
        email = terminal_read.email()
        user = user_services.get_user_by_email(email)
        if(user == Email.DOES_NOT_EXIST):
            console.statement(f'{email} does not exists. Please try again.')
        else:
            console.statement(
                f'Welcome {user["first_name"]} {user["last_name"]}!')
            return

        answer = terminal_read.yes_no()
        if answer == Answer.NO:
            return


def register():
    name = terminal_read.name()
    email = terminal_read.email()
    phone_number = terminal_read.phone_number()
    pwd = terminal_read.password()

    user_services.add_user_to_json(name, email, pwd, phone_number)


def forgot_password():
    phone_number = terminal_read.phone_number()

    pwd = terminal_read.password()

    # Read email
    email = terminal_read.email()

    # Read name
    name = terminal_read.name()

    # Read phone number

    # Read password
    pass

# 015770464441
