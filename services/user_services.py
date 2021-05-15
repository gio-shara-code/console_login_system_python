import json
from os import confstr
from enums.instance import Instance
from enums.option import Option
from models.user import User


f = open("users.json")
users = json.load(f)


def get_user_by_email(email: str) -> User:
    for user in users:
        if(user["email"] == email):
            return User.from_json(user)
    return Instance.DOES_NOT_EXIST


def add_user_to_json(user: User):
    with open("users.json", "r+") as file:
        data = json.load(file)
        data.append(user.to_json())
        file.seek(0)
        json.dump(data, file, indent=4)


def get_user_by_phone_number(phone_number: str) -> User:
    for user in users:
        if(user["phone_number"] == phone_number):
            return User.from_json(user)
    return Instance.DOES_NOT_EXIST
