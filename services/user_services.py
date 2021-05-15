import json
from os import confstr
from enums.email import Email
from enums.option import Option


f = open("users.json")
users = json.load(f)


def get_user_by_email(email: str):
    for user in users:
        if(user["email"] == email):
            return user
    return Email.DOES_NOT_EXIST


def add_user_to_json(name: str, email: str, pwd: str, phone_number: str):
    with open("users.json", "r+") as file:
        data = json.load(file)["users"]
        data.append({
            "name": name,
            "email": email,
            "password": pwd,
            "phone_number": phone_number
        })
        file.seek(0)
        json.dump(data, file)
