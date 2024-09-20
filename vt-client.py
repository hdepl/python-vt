#Virtual Trading Application - Version 1.0

import mysql.connector    #connector for MySQL
import time               #time library module 
import math               #math library module 
#database credentials will be changed once after completion of the project
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
#cursor object for running the sql querries
mycursor = mydb.cursor()


