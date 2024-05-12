#Write a program to establish MySql connectivity with python to insert/update records in a table.
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="test"
)

# Get a cursor object
cursor = db.cursor()

def insert(name, email):
    # Insert a new record
    sql = "INSERT INTO users (name, email) VALUES ('{}','{}')".format(name, email)
    # values = ("John Doe", "john@example.com")
    cursor.execute(sql)
    db.commit()
    print(f"{cursor.rowcount} record inserted.")

def update(name, email):
    # Update an existing record
    sql = "UPDATE users SET name = '{}' WHERE email = '{}'".format(name, email)
    # values = ("newemail@example.com", "John Doe")
    cursor.execute(sql)
    db.commit()
    print(f"{cursor.rowcount} record updated.")

print("\nWhich Operation do you want to perform:\n")
print("-----------1. Insert Record-----------")
print("-----------2. Update Record-----------")
choice=int(input())
if(choice==1):
    name=input("Enter name; ")
    email=input("Enter e-mail; ")
    insert(name,email)
elif(choice==2):
    email=input("Enter email of which you want to update record: ")
    name=input("Enter Updated Name: ")
    update(name, email)
else:
    print("Invalid Key")

# Close the cursor and connection
cursor.close()
db.close()
