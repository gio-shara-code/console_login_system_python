import json

f = open("data.json")
users = json.load(f)["users"]


def get_user_by_id(id: int):
    for user in users:
        if(user["userId"] == id):
            return user
    return -1


def get_user_by_email(emailAddress: str):
    for user in users:
        if(user["emailAddress"] == emailAddress):
            return user
    return -1


# founded_user_by_id = get_user_by_id(1)
# if(founded_user_by_id == -1):
#     print("User couldn't be found")


# founded_user_by_email = get_user_by_email("krish.lee@learningcontainer.com")
# if(founded_user_by_email == -1):
#     print("User couldn't be found")

print("### Welcome ###")
print("### 1. Login ###")

optionIsInvalid = True
while optionIsInvalid:
    option = input("Please input your option: ")
    try:
        option = int(option)
        optionIsInvalid = False
    except:
        print(f'{option} is not an appropriate option')


def login():
    email = input("Please input your email: ")
    # Format of email
    user = get_user_by_email(email)
    if(user == -1):
        print(f'{email} does not exists.')
    else:
        print(f'Welcome {user["firstName"]} {user["lastName"]}')


if option == 1:
    login()


# krish.lee@learningcontainer.com
