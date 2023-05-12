from utils.db import Db as sql
from termcolor import colored
from sys import argv, exit
import questionary

def main():
    db = sql()

    print(db.list())
    print(db.add("Hello, World!"))
    


if __name__ == "__main__":
    main()



