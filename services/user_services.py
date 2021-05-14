import json
from os import confstr
from enums.email import Email
from enums.option import Option



f = open("users.json")
users = json.load(f)["users"]

def get_user_by_email(email_address: str):
    for user in users:
        if(user["emailAddress"] == email_address):
            return user
    return Email.DOES_NOT_EXIST


