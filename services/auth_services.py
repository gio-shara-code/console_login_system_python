from enums.answer import Answer
from utils import console
from services import user_services
from utils import terminal_read
from enums.instance import Instance
from models.user import User
from api import sms
from enums.process import Process


def login():
    while True:
        email = terminal_read.email()
        user = user_services.get_user_by_email(email)
        if(user == Instance.DOES_NOT_EXIST):
            console.statement(
                f'{email} does not exists. Please try again.')
        else:
            # Check whether password is correct
            while True:
                password = terminal_read.password()
                if password == user.get_password():
                    return console.successful_message(
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

    while True:
        email = terminal_read.email()
        user = user_services.get_user_by_email(email)

        if user != Instance.DOES_NOT_EXIST:
            console.warning(
                f'{email} does already exists. Please try again.')
            continue
        break

    pwd = terminal_read.password()
    phone_number = terminal_read.phone_number()

    # instead of 23 random number
    user = User(23, name, email, pwd, phone_number)
    user_services.add_user_to_json(user)


def forgot_password():
    # read phone number
    # and send the user a message with his password via phone.
    while True:
        phone_number = terminal_read.phone_number()
        user = user_services.get_user_by_phone_number(phone_number)
        if user == Instance.DOES_NOT_EXIST:
            console.warning(
                f"{phone_number} does not exists. Please try again")
            continue
        process = sms.send_password(phone_number, user.get_password())
        if process == Process.FAILED:
            return console.warning("Your phone number doesn't exist.")
        console.successful_message(
            "We sent you your password on your phone. Good Luck and don't forget it next time!")
        break
