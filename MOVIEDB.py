import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="P@yal1999")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE MOVIEDB")
print("Database has been created")
