import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'library',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS user(
        ID INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(225),
        email VARCHAR(225),
        phonenumber VARCHAR(225),
        date1 date,
        date2 date,
        PRIMARY KEY(ID)
    )
    """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS attendant(
      username VARCHAR(100),
      password VARCHAR(100)
    )"""
)

