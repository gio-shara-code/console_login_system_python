from utils import theme

def options():
    print(theme.option("1. Login"))
    print(theme.option("2. Register"))

def headline(headline: str):
    print(theme.headline(f'\n### {headline.upper()} ###\n'))
