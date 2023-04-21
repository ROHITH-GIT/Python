import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="@123"
)
print("Connection Successful!!!")
mycursor = mydb.cursor()


print("Welcome to Hyderabad Metro")
print("Please Choose anyone from the below")
print("1.Registration")
print("2.Travel")
print("3.Check Balance")
value = int(input("Please enter your choice :"))

if value ==1:
    print("you have choosed to register")
    print("Please provide the required details for registration")
    def userRegistration():
        print("Name,Phone number,age : ")
        Name,Phone_number,age=input().split(',')
        #print("{},{},{}".format(Name,Phone_number,age))
        mycursor.execute("CREATE  DATABASE IF NOT EXISTS METRO")
        mycursor.execute("CREATE TABLE IF NOT EXISTS METRO.Customer (Name VARCHAR(50),Phone_number INTEGER,age INTEGER)")
        mycursor.execute("INSERT INTO METRO.Customer(Name,Phone_number,age) values(%s,%s,%s) ",(Name,Phone_number,age))
        mydb.commit()
        print(mycursor.rowcount,"records inserted successfully")
    userRegistration()
