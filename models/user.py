class User:
    def __init__(self, user_id=None, name=None, email=None, pwd=None, phone_number=None) -> None:
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__pwd = pwd
        self.__phone_number = phone_number

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

    def welcome_text(self):
        return f'Welcome! Your have been successfully authenticated {self.__name}!'

    def sent_sms_success_text(self):
        return f'{self.__name}, we sent you your password via sms.\nGood Luck and don\'t forget it next time!'

    def successfully_registered_text(self):
        return f'{self.__name}, you have been successfully registered.'
