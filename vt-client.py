#Virtual Trading Application - Version 1.0

import mysql.connector    #connector for MySQL
import time               #time library module 
import math               #math library module 
#database credentials will be changed once after completion of the project
#Demo db is used for production 
mydb = mysql.connector.connect(
  host="103.211.216.137",
  user="kivaabip_stocks",
  password="hdepl@2020",
  database="kivaabip_stockmarket"
)
#cursor object for running the sql querries
mycursor = mydb.cursor()

cashbal = 0
holdingbal = 0
overallbal = 0

def dashboard():
    sql1 = "SELECT * FROM account WHERE username = %s"
    val1 = (username, )
    mycursor.execute(sql1, val1)
    row1 = mycursor.fetchall()
    for x in row1:
        cashbal = x[2]
        holdingbal = x[3]
        overallbal = x[4]
    print("Dashboard")
    print("Cash Balance    : ₹", cashbal)
    print("Holding Balance : ₹", holdingbal)
    print("Overall Balance : ₹", overallbal)
    
username = int(input("Enter your Mobile Number : "))
password = input("Enter the password : ")

#print("Username : ", username)
#print("Password : ", password)

sql = "SELECT * FROM customers WHERE username = %s"
value = (username, )
mycursor.execute(sql, value)

row = mycursor.fetchone()

if(password == row[2]):
    print("Login Verified")
    dashboard()
    
