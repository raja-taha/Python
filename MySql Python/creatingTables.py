import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pythonDatabase"
)

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE IF NOT EXISTS Person (personId INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), age SMALLINT UNSIGNED)")

# mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ('Talha', 21))
# db.commit()

mycursor.execute("SELECT * FROM Person")
for x in mycursor:
    print(x)