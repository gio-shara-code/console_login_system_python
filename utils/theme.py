from termcolor import colored

def input(text: str):
    return colored(f'{text}', "cyan")

def warning(text: str):
    return colored(f'{text}', "red")

def option(text: str):
    return colored(f'{text}', "magenta", attrs=['bold'])

def headline(text: str):
    return colored(f'{text}', 'blue', attrs=['bold'])