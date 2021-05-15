from enums.answer import Answer
from utils import console
from services import user_services
from utils import terminal_read
from enums.email import Email


def login():
    while True:
        email = terminal_read.email()
        password = terminal_read.password()

        user = user_services.get_user_by_email(email)
        if(user == Email.DOES_NOT_EXIST):
            console.statement(
                f'{user.get_email()} does not exists. Please try again.')
        else:
            # Check whether password is correct
            # If wrong, yes or no?

            console.statement(
                f'Your are authenticated {user.get_name()}!')
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

# 015770464441
