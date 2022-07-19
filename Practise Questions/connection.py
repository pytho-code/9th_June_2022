import pymysql

con=pymysql.connect(host="localhost",user="admin",password="12345")
mydb=con.cursor()
print(con)
mydb.execute("create database tops ")
con.commit()





