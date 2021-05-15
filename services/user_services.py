import json
from os import confstr
from enums.email import Email
from enums.option import Option
from models.user import User


f = open("users.json")
users = json.load(f)


def get_user_by_email(email: str) -> User:
    for user in users:
        if(user["email"] == email):
            return User.from_json(user)
    return Email.DOES_NOT_EXIST


def add_user_to_json(name: str, email: str, pwd: str, phone_number: str):
    with open("users.json", "r+") as file:
        data = json.load(file)
        data.append({
            "name": name,
            "email": email,
            "password": pwd,
            "phone_number": phone_number
        })
        file.seek(0)
        json.dump(data, file, indent=4)
