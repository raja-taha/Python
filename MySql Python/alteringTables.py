from datetime import datetime
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pythonDatabase"
)

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE IF NOT EXISTS Test (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL)")

# mycursor.execute("INSERT INTO Test (name,created, gender) VALUES (%s, %s, %s)", ('Sana', datetime.now(), 'F'))
# db.commit()

# mycursor.execute("SELECT * FROM Test WHERE gender = 'M' ORDER BY id DESC")
# mycursor.execute("SELECT id, gender FROM Test WHERE gender = 'M' ORDER BY id DESC")

# mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(100) NOT NULL ")
# mycursor.execute("ALTER TABLE Test DROP food")
# mycursor.execute("ALTER TABLE Test CHANGE IF EXISTS first_name name VARCHAR(255)")

mycursor.execute("DESCRIBE Test")
for x in mycursor:
    print(x)