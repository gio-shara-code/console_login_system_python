import json


def get_all_users() -> list:
    f = open("users.json")
    users = json.load(f)
    f.close()
    return users


def write_users(new_users: str):
    with open("users.json", "w") as file:
        file.write(new_users)
        pass
