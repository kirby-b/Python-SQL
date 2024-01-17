import mysql.connector
def main():
    mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="thedatabase"
    )

    mycursor = mydb.cursor()

    sql = "DROP TABLE customers"

    mycursor.execute(sql)


if __name__ == '__main__':
    main()