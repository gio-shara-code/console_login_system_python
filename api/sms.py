import os
from twilio.rest import Client
from dotenv import load_dotenv
from enums.process import Process
load_dotenv()

def send_password(to: str, password: str):
    account_sid = os.environ.get('twilio_account_sid')
    auth_token = os.environ.get('twilio_auth_token')
    phone_number = os.environ.get('twilio_phone_number')

    client = Client(account_sid, auth_token)
    try:
        client.messages.create(
            to=to,
            from_=phone_number,
            body=f'Your password is: {password}')
    except:
        return Process.FAILED
    return Process.SUCCEEDED
