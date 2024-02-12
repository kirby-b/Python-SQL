import mysql.connector


def main():
    db = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="thedatabase"
    )   
    #Creates a connection
    dbcursor.execute("CREATE TABLE memes (name VARCHAR(255), score VARCHAR(255))")
    sql = "INSERT INTO memes (name, score) VALUES (%s, %s)"
    val = ("Rick Roll", "11/10")
    dbcursor.execute(sql, val)
    sql = "INSERT INTO memes (name, score) VALUES (%s, %s)"
    val = ("Anything from vine", "10/10")
    dbcursor.execute(sql, val)
    sql = "INSERT INTO memes (name, score) VALUES (%s, %s)"
    val = ("Bee Movie Script", "10/10")
    dbcursor.execute(sql, val)
    #Sends commands
    db.commit()
    #Commits them
    dbcursor.execute("SELECT * FROM memes")
        
    my_result = mycursor.fetchall()

    for x in my_result:
        print(x)

if __name__ == '__main__':
    main()
