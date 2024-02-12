import mysql.connector


def main():
    db = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword"
    )
    #Creates a connection to the DB
    dbcursor = db.cursor()
    dbcursor.execute("CREATE DATABASE mydatabase")
    

if __name__ == '__main__':
    main()
