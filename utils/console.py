from termcolor import colored, cprint

def options():
    print(colored('1. Login', 'magenta', attrs=['bold']))
    print(colored('2. Register/n', 'magenta', attrs=['bold']))

def headline(headline: str):
    print(colored(f'\n### {headline.upper()}! ###', 'blue', attrs=['bold']))