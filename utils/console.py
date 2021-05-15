import theme


def options():
    print(theme.option("1. Login"))
    print(theme.option("2. Register"))
    print(theme.option("3. Forgot Password"))
    print(theme.option("4. Reset Password\n"))


def headline(text: str):
    print(theme.headline(f'\n### {text.upper()} ###\n'))


def warning(text: str):
    print(f'{theme.red_bold("Warning: ")}{theme.bold_white(f"{text}")}\n')


def question(text: str):
    print(f'{theme.yellow_bold(f"{text}")}{theme.bold_white(f"{text}")}\n')


def statement(text: str):
    print(f'{theme.bold_white(f"{text}")}\n')


def successful_message(text: str):
    print(f'{theme.green_bold(f"{text}")}\n')

