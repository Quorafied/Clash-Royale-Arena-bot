# Importing main modules
import mysql.connector


# Create database class for database connection
class sqlDatabase():
    def __init__(self):
        self.mydb = None
        self.cursor = None

    # Establish connection to database
    def connect(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="admin",
            autocommit = True
        )
    
    # Set up cursor to database
    def setCursor(self):
        self.cursor = self.mydb.cursor()
    
    # Create database
    def createDatabase(self, name):
        self.cursor.execute(
            """CREATE
            DATABASE
            IF NOT EXISTS
            {}""".format(name))
