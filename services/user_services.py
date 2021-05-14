import json
 
f = open("users.json")
users = json.load(f)["users"]

def get_user_by_email(email_address: str):
    for user in users:
        if(user["emailAddress"] == email_address):
            return user
    return -1
