from utils import validate
import theme
from utils import console
from enums.answer import Answer


def option():
    while True:
        try:
            option = int(input(theme.input("Option: ")))
            if validate.option(option) == Answer.CORRECT:
                return option
            console.warning("Wrong option, try again")
        except:
            console.warning("Please input only numbers")


def email():
    while True:
        email = input(theme.input("Email: "))
        if validate.email(email) == Answer.NOT_CORRECT:
            console.warning("Invalid email format, please try again.")
        else:
            return email


def name():
    while True:
        name = input(theme.input("Name (e.g. Robert Schulz): "))
        if validate.name(name) == Answer.NOT_CORRECT:
            console.warning(
                "Name should only contain charachters.")
        else:
            return name


def phone_number():
    while True:
        phone_number = input(theme.input(
            "Phone Number: (e.g. +4915574461441): "))
        if validate.phone_number(phone_number) == Answer.NOT_CORRECT:
            console.warning(
                "Phone number should only contain 12 digits")
        else:
            return phone_number


def password(input_text: str):
    while True:
        pwd = input(theme.input(input_text))
        if validate.password(pwd) == Answer.NOT_CORRECT:
            console.warning(
                "Passwords length should be min. 4 and max. 8 and characters only")
        else:
            return pwd


def try_again():
    while True:
        answer = input(theme.yellow_bold("Do you want to try again? (y/n): "))
        if answer.lower() == "n" or answer.lower() == "no":
            console.statement("See you.")
            return Answer.NO
        elif answer.lower() == "y" or answer.lower() == "yes":
            print("")
            return Answer.YES
        else:
            console.statement(
                f"{answer} is not a proper answer, please try again")
