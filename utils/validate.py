import re
from enums.email import Email
def email(email):
    if re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email):
        return Email.CORRECT_FORMAT
    return Email.NOT_CORRECT_FORMAT