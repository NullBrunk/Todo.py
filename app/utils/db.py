import sqlite3

class Db:

    """
    Class pour simplifier la connection a la database et simplifier
    les intéraction avec elle

    
    CREATE TABLE py(
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `task` TEXT NOT NULL,
        `done` BOOLEAN
    ); 
    
    """

    def __init__(self):
        self.connection = sqlite3.connect(__file__.replace('db.py', '') + "../db/db.sqlite")
        self.cursor = self.connection.cursor()

    def list(self) -> list:
        res = self.cursor.execute("SELECT * FROM py")
        return res.fetchall()
        


    def add(self, task: str) -> None:
        
        self.cursor.execute(
            "INSERT INTO py(`id`, `task`, `done`) VALUES(NULL, ?, ?)", 
            (task, 0)
        )
        
        self.connection.commit()

    def mark(self, id: str) -> None:
        self.cursor.execute(
            "UPDATE py SET done=1 WHERE id=?", 
            (id), 
        )
        self.connection.commit()


    def rm(self, id: str) -> None:
        self.cursor.execute(
            "DELETE FROM py WHERE id=?", 
            (id), 
        )
        
        self.connection.commit()



if __name__ == "__main__":
    print("This is part of the TODO List app and is a module used by the main.py file.")
