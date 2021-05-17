class Messages:
    def __init__(self, user_full_name) -> None:
        self.SUCCESSFULLY_REGISTERED = f'{user_full_name}, you have been successfully registered.'
        self.SUCCESSFULLY_SENT_SMS = f'{user_full_name}, we sent you your password via sms.\nGood Luck and don\'t forget it next time!'
        self.SUCCCESFULLY_LOGIN = f'Welcome! Your have been successfully authenticated {user_full_name}!'
        self.SUCCESSFULLY_RESET_PASSWORD = f'{user_full_name}, you have successfully changed your password!'
