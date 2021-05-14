from utils import theme

def options():
    print(theme.option("1. Login"))
    print(theme.option("2. Register\n"))

def headline(text: str):
    print(theme.headline(f'\n### {text.upper()} ###\n'))

def warning(text: str):
    print(f'{theme.red_bold("Warning: ")}{theme.bold(f"{text}")}\n')