import re
from enums.answer import Answer
from enums.option import Option


def option(opt):
    if opt < 1 or opt > len(Option):
        return Answer.NOT_CORRECT
    return Answer.CORRECT


def email(email: str):
    if re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email.strip()):
        return Answer.CORRECT
    return Answer.NOT_CORRECT


def name(name: str):
    if re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name):
        return Answer.CORRECT
    return Answer.NOT_CORRECT


def password(pwd: str):
    if re.fullmatch('[A-Za-z]{4,8}?', pwd):
        return Answer.CORRECT
    return Answer.NOT_CORRECT


def phone_number(phone_number: str):
    if re.fullmatch('^\d{12}$', phone_number):
        return Answer.CORRECT
    return Answer.NOT_CORRECT
