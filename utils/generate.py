from datetime import datetime


def random_id() -> str:
    now = datetime.now()
    return f'{now.microsecond}{now.second}'
