from enums.answer import Answer
from utils import console
from services import user_services
from utils import terminal_read
from enums.email import Email
from models.user import User


def login():
    while True:
        email = terminal_read.email()
        user = user_services.get_user_by_email(email)
        if(user == Email.DOES_NOT_EXIST):
            console.statement(
                f'{email} does not exists. Please try again.')
        else:
            # Check whether password is correct
            while True:
                password = terminal_read.password()
                if password == user.get_password():
                    return console.statement(
                        f'Your are authenticated {user.get_name()}!')
                else:
                    console.statement(
                        f'Wrong password!')
                    answer = terminal_read.yes_no()
                    if answer == Answer.NO:
                        return

        answer = terminal_read.yes_no()
        if answer == Answer.NO:
            return


def register():
    name = terminal_read.name()
    email = terminal_read.email()
    pwd = terminal_read.password()
    phone_number = terminal_read.phone_number()

    # instead of 23 random number
    user = User(23, name, email, pwd, phone_number)
    user_services.add_user_to_json(user)


def forgot_password():
    phone_number = terminal_read.phone_number()

# 015770464441
