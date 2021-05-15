import json
from os import confstr
from enums.instance import Instance
from models.user import User
from services import file_services


def get_user_by_email(email: str) -> User:
    users = file_services.get_all_users()
    for user in users:
        if(user["email"] == email):
            return User.from_json(user)
    return Instance.DOES_NOT_EXIST


def add_user_to_json(user: User):
    users = file_services.get_all_users()
    users.append(user.to_json())
    new_users = json.dumps(users)
    file_services.write_users(new_users)


def get_user_by_phone_number(phone_number: str) -> User:
    users = file_services.get_all_users()
    for user in users:
        if(user["phone_number"] == phone_number):
            return User.from_json(user)
    return Instance.DOES_NOT_EXIST


def replaced_users_password(new_password: str, email: str):
    users = file_services.get_all_users()
    for user in users:
        if user["email"] == email:
            user["password"] = new_password
    new_users = json.dumps(users)
    file_services.write_users(new_users)

### Features ###
# 1. Generate random id's
