class User:
    def __init__(self, user_id, name, email, pwd, phone_number) -> None:
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__pwd = pwd
        self.__phone_number = phone_number
        self.SUCCESSFULLY_REGISTERED = f'{name}, you have been successfully registered.'
        self.SUCCESSFULLY_SENT_SMS = f'{name}, we sent you your password via sms.\nGood Luck and don\'t forget it next time!'
        self.WELCOME = f'Welcome! Your have been successfully authenticated {name}!'

    def get_email(self):
        return self.__email

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__pwd

    def get_phone_number(self):
        return self.__phone_number

    @staticmethod
    def from_json(json: object):
        return User(json['user_id'], json['name'], json['email'], json['password'], json['phone_number'])

    def to_json(self):
        return {
            "user_id": self.__user_id,
            "name": self.__name,
            "phone_number": self.__phone_number,
            "email": self.__email,
            "password": self.__pwd
        }
