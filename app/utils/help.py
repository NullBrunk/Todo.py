from termcolor import colored

def h():
    """
    Local HELP function for this todo app
    """

    print(f"""
┬───────────────────────────┬
│ {colored("TUI Mode ", 'blue', attrs=['bold']) }:                │
┼───────────────────────────┼
│                           │ 
│   {colored('main.py', 'white', attrs=["bold"])}                 │
│                           │ 
┼───────────────────────────┼
│ {colored("CLI Mode ", 'blue', attrs=['bold']) }:                │
┼───────────────────────────┼
│                           │ 
│   {colored('main.py', 'white', attrs=["bold"])} {colored('list', 'red', attrs=["bold"])}            │
│   {colored('main.py', 'white', attrs=["bold"])} {colored('add', 'red', attrs=["bold"])}             │    
│   {colored('main.py', 'white', attrs=["bold"])} {colored('rm', 'red', attrs=["bold"])}              │
│                           │
┴───────────────────────────┴
    """)

def addhelp():
    print(f"""\n┬──────────────────────────────┬
│ {colored("./main.py", 'white')} {colored("add", 'red', attrs=["bold"])} "Some tasks"   │ 
┴──────────────────────────────┴
    """)

def rmhelp():
    print(f"""\n┬──────────────────────────────┬
│      {colored("./main.py", 'white')} {colored("rm", 'red', attrs=["bold"])} ID         │ 
┴──────────────────────────────┴
    """)

if __name__ == "__main__":
    print("This is part of the TODO List app and is a module used by the main.py file.")
