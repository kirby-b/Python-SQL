import mysql.connector


def main():
    db = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword"
    )
    dbcursor = db.cursor()
    dbcursor.execute("CREATE DATABASE mydatabase")
    dbcursor.execute("CREATE TABLE memes (name VARCHAR(255), score VARCHAR(255))")


if __name__ == '__main__':
    main()
