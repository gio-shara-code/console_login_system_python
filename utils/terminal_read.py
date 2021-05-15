from utils import validate
from utils import theme
from utils import console
from enums.answer import Answer
from enums.email import Email
from enums.input import Input


def option():
    while True:
        try:
            option = int(input(theme.input("Option: ")))
            if validate.option(option) == Input.CORRECT_FORMAT:
                return option
            console.warning("Wrong option, try again")
        except:
            console.warning("Wrong option, try again")


def email():
    while True:
        email = input(theme.input("Email: "))
        if validate.email(email) == Input.NOT_CORRECT_FORMAT:
            console.warning("Invalid email format, please try again.")
        else:
            return email


def name():
    while True:
        name = input(theme.input("Name (e.g. Robert Schulz): "))
        if validate.name(name) == Input.NOT_CORRECT_FORMAT:
            console.warning(
                "Name should only contain charachters.")
        else:
            return name


def phone_number():
    while True:
        phone_number = input(theme.input("Phone Number (e.g. 015770464441): "))
        if validate.phone_number(phone_number) == Input.NOT_CORRECT_FORMAT:
            console.warning(
                "Phone number should only contain 12 digits")
        else:
            return phone_number


def password():
    while True:
        pwd = input(theme.input("Password (min. 4 and max. 8 characters): "))
        if validate.password(pwd) == Input.NOT_CORRECT_FORMAT:
            console.warning(
                "Passwords length should be min. 4 and max. 8 and characters only")
        else:
            return pwd


def yes_no():
    while True:
        answer = input(theme.yellow_bold("Do you want to try again? (y/n): "))
        if answer.lower() == "n":
            console.statement("See you.")
            return Answer.NO
        elif answer.lower() == "y":
            return Answer.YES
        else:
            console.statement(
                f"{answer} is not a proper answer, please try again")
