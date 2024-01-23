import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pythonDatabase"
)

users = [('Taha', 'taha123'),
         ('Talha', 'talha123'),
         ('Saif', 'saif123')]

user_scores = [(45, 100),
               (30, 200),
               (46, 124)]

mycursor = db.cursor()

# Q1 = "CREATE TABLE IF NOT EXISTS Users (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL)"
# Q2 = "CREATE TABLE IF NOT EXISTS Scores (userId INT PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 INT DEFAULT 0, game2 INT DEFAULT 0)"

# mycursor.execute(Q1)
# mycursor.execute(Q2)

# Q3 = "INSERT INTO Users (name, password) VALUES (%s, %s)"
# Q4 = "INSERT INTO Scores (userId, game1, game2) VALUES (%s, %s, %s)"

# for x, user in enumerate(users):
#     mycursor.execute(Q3, user)
#     last_id = mycursor.lastrowid
#     mycursor.execute(Q4, (last_id,) + user_scores[x])

# db.commit()

mycursor.execute("SELECT * FROM Users")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM Scores")
for x in mycursor:
    print(x)