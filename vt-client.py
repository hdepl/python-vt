#Virtual Trading Application - Version 1.0

import mysql.connector    #connector for MySQL
import time               #time library module 
import math               #math library module 
#database credentials will be changed once after completion of the project
mydb = mysql.connector.connect(
  host="103.211.216.137",
  user="kivaabip_stocks",
  password="hdepl@2020",
  database="kivaabip_stockmarket"
)
#cursor object for running the sql querries
mycursor = mydb.cursor()

username = int(input("Enter your Mobile Number : "))
password = input("Enter the password : ")

#print("Username : ", username)
#print("Password : ", password)

