from enums.answer import Answer
from utils import console_log
from services import user_services
from utils import terminal_read
from enums.instance import Instance
from models.user import User
from api import sms
from enums.process import Process
from utils import generate


def login():
    while True:
        email = terminal_read.email()
        user = user_services.get_user_by_email(email)
        if(user == Instance.DOES_NOT_EXIST):
            console_log.statement(
                f'{email} does not exists.')
            answer = terminal_read.try_again()
            if answer == Answer.NO:
                return
            continue
        break

    while True:
        password = terminal_read.password("Password: ")
        if password == user.get_password():
            return console_log.success(user.messages.SUCCCESFULLY_LOGIN)
        else:
            console_log.statement(
                f'Wrong password!')
            answer = terminal_read.try_again()
            if answer == Answer.NO:
                return


def register():
    name = terminal_read.name()

    while True:
        email = terminal_read.email()
        user = user_services.get_user_by_email(email)
        if user != Instance.DOES_NOT_EXIST:
            console_log.warning(
                f'{email} does already exist. Please try again.')
            continue
        break

    pwd = terminal_read.password("Password (min. 4 and max. 8 characters): ")
    phone_number = terminal_read.phone_number()

    user = User(generate.random_id(), name, email, pwd, phone_number)
    user_services.add_user_to_json(user)
    console_log.success(user.messages.SUCCESSFULLY_REGISTERED)


def forgot_password():
    while True:
        phone_number = terminal_read.phone_number()
        user = user_services.get_user_by_phone_number(phone_number)
        if user == Instance.DOES_NOT_EXIST:
            console_log.warning(
                f"{phone_number} does not exists. Please try again.")
            continue

        process = sms.send_password(phone_number, user.get_password())

        if process == Process.FAILED:
            return console_log.warning("Your phone number doesn't exist.")
        console_log.success(user.messages.SUCCESSFULLY_SENT_SMS)
        break


def reset_password():
    while True:
        email = terminal_read.email()
        user = user_services.get_user_by_email(email)
        if(user == Instance.DOES_NOT_EXIST):
            console_log.statement(
                f'{email} does not exists. Please try again.')
            continue
        break

    while True:
        current_password = terminal_read.password("Current Password: ")
        if current_password != user.get_password():
            console_log.statement(
                f'Wrong password!')
            answer = terminal_read.try_again()
            if answer == Answer.NO:
                return
            continue
        break

    new_password = terminal_read.password("New Password: ")
    user_services.replaced_users_password(new_password, email)
    console_log.success(user.messages.SUCCESSFULLY_RESET_PASSWORD)
