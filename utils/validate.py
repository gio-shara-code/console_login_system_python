import re
from enums.input import Input
from enums.option import Option


def option(opt):
    if opt < 1 or opt > len(Option):
        return Input.NOT_CORRECT_FORMAT
    return Input.CORRECT_FORMAT


def email(email: str):
    if re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email):
        return Input.CORRECT_FORMAT
    return Input.NOT_CORRECT_FORMAT


def name(name: str):
    if re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name):
        return Input.CORRECT_FORMAT
    return Input.NOT_CORRECT_FORMAT


def password(pwd: str):
    if re.fullmatch('[A-Za-z]{4,8}?', pwd):
        return Input.CORRECT_FORMAT
    return Input.NOT_CORRECT_FORMAT


def phone_number(phone_number: str):
    if re.fullmatch('^\d{12}$', phone_number):
        return Input.CORRECT_FORMAT
    return Input.NOT_CORRECT_FORMAT
