#Virtual Trading Application - Version 1.0

import mysql.connector    #connector for MySQL
import time               #time library module 
import math               #math library module 
from os import system, name     #system library module

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

username = 0
cashbal = 0
holdingbal = 0
overallbal = 0

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def mainmenu():
    print("Main Menu")
    print("1: View Balance")
    print("2: Trade")
    print("3: Exit")
    opt = int(input("Choose an Option : "))

    match opt:
        case 1:
            balance()
        case 2:
            trade()
        case 3:
            exit()
        case _:
            print("Error : Select a valid Option.")
            mainmenu()

def balance():
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
    
def trade():
    print("Trade")

def start():
    print("1 : Login")
    print("2 : Sign Up")
    opt1 = int(input("Select an Option : "))
    match opt1:
        case 1:
            login()
        case 2:
            signup()
        case _:
            exit()

def login():
    global username
    username = int(input("Enter your Mobile Number : "))
    password = input("Enter the password : ")

    sql = "SELECT * FROM customers WHERE username = %s"
    value = (username, )
    mycursor.execute(sql, value)

    row = mycursor.fetchone()

    if(password == row[2]):
        print("Login Verified")
        mainmenu()
    else:
        print("Invalid Username or Password !")
        print("Relaunch the application")

def signup():
    username = int(input("Enter your mobile number : ")) 
    sql2 = "SELECT * FROM customers WHERE username = %s"
    val2 = (username, )
    mycursor.execute(sql2, val2)
    row2 = mycursor.fetchone()
    print(row2)
    if(row2 != None):
        print("Username already exists")
        print("Choose other username or Login if already Signed Up")
        signup()
    password = input("Enter the Password (a-z, A-Z, 0-9, !@#$& ) : ")
    
    sql3 = "INSERT INTO customers (username, password) VALUES (%s, %s)"
    val3 = (username, password)
    mycursor.execute(sql3, val3)
    mydb.commit()

    sql4 = "INSERT INTO account (username, cashbal, holdingbal, overallbal) VALUES (%s, %s, %s, %s)"
    val4 = (username, 100000, 0, 100000)
    mycursor.execute(sql4, val4)
    mydb.commit()

    print("User Account Created, login to your account.")
    login()

clear()

start()
