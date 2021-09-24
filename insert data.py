import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="P@yal1999", database="MOVIEDB")
mycursor = mydb.cursor()
Sql = "INSERT INTO Movies (NAME, ACTOR, ACTRESS, DIRECTOR, YOR) VALUE (%s,%s,%s,%s,%s)"
val = ('SHERSHAH','SIDDHARTH MALHOTRA',
 'KIARA ADVANI', 'VISHNU VARDHAN', '2021')
Sql1 = "INSERT INTO Movies (NAME, ACTOR, ACTRESS, DIRECTOR, YOR) VALUE (%s,%s,%s,%s,%s)"
val1= ('MIMI','PANKAJ TRIPATHI',
 'KIRTI SANON', 'LAXMAN UTEKAR', '2021')
Sql2 = "INSERT INTO Movies (NAME, ACTOR, ACTRESS, DIRECTOR, YOR) VALUE (%s,%s,%s,%s,%s)"
val2 = ('ENTERTAINMENT','AKSHAY KUMAR',
 'TAMANAAH BHATIA', 'FARHAD SAMJI', '2014')
mycursor.execute(Sql,val)
mycursor.execute(Sql1,val1)
mycursor.execute(Sql2,val2)
mydb.commit()
print("record inserted.")
