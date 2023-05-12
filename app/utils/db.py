import sqlite3

class Db:

    """
    Class pour simplifier la connection a la database et simplifier
    les intéraction avec elle

    
    CREATE TABLE py(
        `id` INT AUTO_INCREMENT PRIMARY KEY,
        `task` TEXT NOT NULL,
        `done` BOOLEAN
    ); 
    
    """

    def __init__(self):
        self.connection = sqlite3.connect("db/db.sqlite")
        self.cursor = self.connection.cursor()

    def selectall(self):
        res = self.cursor.execute("SELECT * FROM py")
        return res.fetchall()
    
    def add(self, task):
        
