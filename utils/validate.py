import re
from enums.answer import Answer
from enums.option import Option


def option(opt):
    if opt < 1 or opt > len(Option):
        return Answer.IN_WRONG_FORMAT
    return Answer.IN_RIGHT_FORMAT


def email(email: str):
    if re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email.strip()):
        return Answer.IN_RIGHT_FORMAT
    return Answer.IN_WRONG_FORMAT


def name(name: str):
    if re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name.strip()):
        return Answer.IN_RIGHT_FORMAT
    return Answer.IN_WRONG_FORMAT


def password(pwd: str):
    if re.fullmatch('[A-Za-z]{4,8}?', pwd):
        return Answer.IN_RIGHT_FORMAT
    return Answer.IN_WRONG_FORMAT


def phone_number(phone_number: str):
    if re.fullmatch('^\+\d{13}$', phone_number.strip()):
        return Answer.IN_RIGHT_FORMAT
    return Answer.IN_WRONG_FORMAT
