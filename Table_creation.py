import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="P@yal1999",database="MOVIEDB")
mycursor = mydb.cursor()
sql = '''CREATE TABLE movies(
   NAME CHAR(20) NOT NULL,
   Actor CHAR(20),
   Actress CHAR(20),
   Director CHAR(20),
   YOR INT(10)
)'''
mycursor.execute(sql)
print("Table has been created")
