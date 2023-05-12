from utils.db import Db as sql
from termcolor import colored
from utils.help import *
from sty import ef, rs
from os import system
from sys import argv
import questionary


def ls(tasks: list):
    if len(tasks) == 0:
        print("No tasks !")

    else:
        for task in tasks:

            print(f"{colored(task[0], 'blue', attrs=['bold'])}: ", end="")

            if task[2] == 1:
                print(ef.strike + task[1] + rs.all)
            else:
                print(task[1])

def showchoices(db) -> str:
    return questionary.select(
        " ",
        instruction="  ",
        choices=[i[1] for i in db.list()],
        qmark=" "
    ).ask()

def tuimode(db):

    while True:
        q = questionary.select(
            " ",
            instruction="  ",
            choices=[
                "Add",
                "List",
                "Mark",
                "Remove",
                "Quit"
            ],
            qmark=" "
        ).ask()

        system("clear || cls")

        match q:
            case "Add":
                db.add(input(": "))
            case "List":
                ls(db.list())
            
            case "Mark":        
                db.mark(str(db.getidbyelement(showchoices(db))[0]))

            case "Remove":
                db.rm(str(db.getidbyelement(showchoices(db))[0]))
            
            case "Quit":
                break
            



    """
    
    
    directory = questionary.select(
        " ",
        instruction="  ",
        choices=t,
        qmark=" "
    ).ask()
"""


def main(argv):
    
    db = sql()
    
    if not argv:
        system("clear || cls")
        tuimode(db)
    
    else:
        match argv[0].lower():
            case "list":
                ls(db.list())
            
            case "add":
                try:
                    db.add(argv[1])
                except IndexError:
                    addhelp()

            case "mark":
                try:
                    db.mark(argv[1])
                except IndexError:
                    mkhelp()   

            case "rm":
                try:
                    db.rm(argv[1])
                except IndexError:
                    rmhelp()

            case others:
                print("Options: List, Add, Rm")


if __name__ == "__main__":
    
    if len(argv) == 1:
        
        main(False)

    else:
        if argv[1] in [ "help", "-h", "--help", "h" ]:
            h()
        
        else:
            main(argv[1:])





