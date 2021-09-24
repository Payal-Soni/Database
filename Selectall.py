import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="P@yal1999", database = "moviedb")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM movies")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)