from utils.help import h, addhelp, rmhelp
from utils.db import Db as sql
from termcolor import colored
from sys import argv, exit
import questionary


def ls(tasks: list):
    if len(tasks) == 0:
        print("No tasks !")
    else:
        for i in tasks:
            print(i)

def main(argv):
    
    db = sql()
    
    if not argv:
        pass
        # TUI MODE
    else:
        match argv[0].lower():
            case "list":
                ls(db.list())
            
            case "add":
                try:
                    db.add(argv[1])
                except IndexError:
                    addhelp()

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





