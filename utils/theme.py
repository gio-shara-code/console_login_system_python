from termcolor import colored

def input(text: str):
    return colored(f'{text}', "cyan")

def option(text: str):
    return colored(f'{text}', "magenta", attrs=['bold'])

def headline(text: str):
    return colored(f'{text}', 'blue', attrs=['bold'])

def red_bold(text: str):
    return colored(f'{text}', 'red', attrs=['bold'])

def bold(text: str):
    return colored(f'{text}', 'white', attrs=['bold'])

# def demand(text: str):
#     return colored(f'{text}', 'red', attrs=['blink'])