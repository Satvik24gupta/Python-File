
import mysql.connector as sql

# User Defined Functions

def menu():
    while True:
        print("My Contacts")
        print("===========")
        print("1. Show Databases")
        print("2. Create Table")
        print("3. Show Tables")
        print("4. Display Table Structure")        
        print('5. Add Contacts')
        print('6. Modify Contacts')
        print('7. Delete Contacts')
        print('8. Display All Records')
        print('9. Query')
        print('0. Exit')
        
        choice=input('Enter choice [0-9]: ')

        if choice == '1':
            showdatabases()
        elif choice == '2':
            createtable()
        elif choice == '3':
            showtables()
        elif choice == '4':
            dispstru()
        elif choice == '5':
            addContacts()
        elif choice == '6':
            modifyContacts()
        elif choice == '7':
            deleteContacts()
        elif choice == '8':
            displayAll()
        elif choice == '9':
            queryMenu()
        elif choice == '0':
            break
        else:
            print('Invalid choice')

def showdatabases():
    con=sql.connect(host='localhost', user='root', passwd='root')

    if not con.is_connected():
        print('Connection failed')
        return

    cursor = con.cursor()
    cursor.execute("show databases")

    print()

    print("Databases")
    print("=========")

    for db in cursor:
        print(db)

    print()
    
    input("Press any key to continue...")
    con.close()

def createtable():
#   DROP TABLE contacts;

    con=sql.connect(host='localhost', user='root', passwd='root', db='test')
    
    if not con.is_connected():
        print('Connection failed')
        return

    cursor = con.cursor()
    cursor.execute("create table contacts (telephone int primary key, fname varchar(20),\
    lname varchar(20), address varchar(50), area varchar(10))")
    
    print("Table created")
    input("Press any key to continue...")
    con.close()

def showtables():
    con=sql.connect(host='localhost', user='root', passwd='root', db='test')

    if not con.is_connected():
        print('Connection failed')
        return

    cursor = con.cursor()
    cursor.execute("show tables")
    
    print()

    print("Tables")
    print("======")

    for tbl in cursor:
        print(tbl)

    print()
    
    input("Press any key to continue...")
    con.close()

def dispstru():
    con=sql.connect(host='localhost', user='root', passwd='root', db='test')

    if not con.is_connected():
        print('Connection failed')
        return

    cursor = con.cursor()
    cursor.execute("desc contacts")

    print()

    print("Structure of CONTACTS table")
    print("===========================")

    print()

    for record in cursor:
        print(record)

    input("\nPress any key to continue...")
    con.close()

def addContacts():
    con=sql.connect(host='localhost', user='root', passwd='root', db='test')
    
    if not con.is_connected():
        print('Connection failed')
        return
    
    cursor=con.cursor()
    
    print('Addition of Contact')
    print('===================')
    
    tel=int(input('Enter Telephone: '))

    # check duplicate telephone numbers
    
    query="SELECT * FROM contacts WHERE telephone={}".format(tel)
    
    cursor.execute(query)
    
    cursor.fetchall()
    
    if cursor.rowcount >= 1:
        input("Duplicate contact numbers NOT allowed. Press any key to continue...")
        con.close()
        return
        
    # Accept rest of the Contacts details
        
    fname=input('Enter First Name: ')
    fname=fname.upper()

    lname=input('Enter Last Name: ')
    lname=lname.upper()


    add=input('Enter Address: ')
    add=add.upper()

    area=input('Enter Area: ')
    area=area.upper()
   
    query="INSERT INTO contacts VALUES ({},'{}','{}','{}','{}')".format(tel,fname,lname,add,area)
    
    ans=input("Want to save (y/n): ")
    
    if ans=='y' or ans=='Y':
        cursor.execute(query)
        con.commit()
        input("Record saved successfully. Press any key to continue...")
    
    con.close()    

def modifyContacts():
    con=sql.connect(host='localhost', user='root', passwd='root', db='test')
    
    if not con.is_connected():
        print('Connection failed')
        return
    
    cursor=con.cursor()
    
    print('Modification of Contacts')
    print('========================')
    
    tel=int(input('Enter Contact Number to modify: '))

    query="SELECT * FROM contacts WHERE telephone={}".format(tel)
    
    cursor.execute(query)
    
    record = cursor.fetchone()
    
    if cursor.rowcount == 0:
        input("Sorry! Record not found. Press any key to continue...")
        con.close()
        return
    
    # Display existing contact details

    print("Record: ", record)

    for field in record:
        print(field, end=' ')

    print()
    
    # Accept new contact details
    
    print()
    print('Enter new contact details')
    print('========================')
    print()
    print('Press Enter for no change')
    print()

    fname=input('Enter First Name: ')
    
    if len(fname)>0:
        fname=fname.upper()
    else:
        fname=record[1]

    lname=input('Enter Last Name: ')

    if len(lname)>0:
        lname=lname.upper()
    else:
        lname=record[2]

    add=input('Enter Address: ')
    
    if len(add)>0:
        add=add.upper()
    else:
        add=record[3]
        
    area=input('Enter Area: ')
    
    if len(area)>0:
        area=area.upper()
    else:
        area=record[3]

    # query="UPDATE contacts SET telephone={}, fname='{}', lname='{}', address='{}', area='{}' WHERE tel={}".format(fname,lname,add,area)
    query="UPDATE contacts SET fname='{}', lname='{}', address='{}', area='{}' WHERE telephone={}".format(fname,lname,add,area,tel)
    
    ans=input("Want to update (y/n): ")
    
    if ans=='y' or ans=='Y':
        cursor.execute(query)
        con.commit()
        input("Record updated successfully")
    
    print("Press any key to continue...")
    
    con.close()    

def deleteContacts():
    con=sql.connect(host='localhost', user='root', passwd='root', db='test')
    
    if not con.is_connected():
        print('Connection failed')
        return
    
    cursor=con.cursor()
    
    print('Deletion of Contacts')
    print('====================')
    
    tel=int(input('Enter Contact Number to delete: '))

    query="SELECT * FROM contacts WHERE telephone={}".format(tel)
    
    cursor.execute(query)

    record = cursor.fetchone()
    
    if cursor.rowcount == 0:
        print("Sorry! Record not found")
        input("Press any key to continue...")
        con.close()
        return
    
    for field in record:
        print(field, end=' ')

    print()

    ans=input('Sure to delete (y/n): ')

    if ans=='y' or ans=='Y':
        query="DELETE FROM contacts WHERE telephone={}".format(tel)
        cursor.execute(query)
        con.commit()
        
        if cursor.rowcount==1:
            print('Record deleted successfully')
        else:
            print('Sorry! Deletion failed')

    input('Press any key to continue...')

    con.close()    

def displayAll():
    print('Display all records')
    print('===================')

    con = sql.connect (host = 'localhost', user = 'root', passwd = 'root', database='test')
    
    if not con.is_connected():
        print("Sorry! Connection failed ......")
        return
    
    cursor = con.cursor()
    
    cursor.execute('SELECT * FROM contacts')

    resultset = cursor.fetchall()

    for row in resultset:
        print(row)

    input("Press any to continue...")    
    con.close()


def queryMenu():
    while True:
        print('Query Menu')
        print('1. Contact Number')
        print('2. First Name')
        print('3. Last Name')
        print('4. Area')
        print('5. Exit')

        choice = int(input('Enter choice [1-5]: '))

        if choice == 1:
            searchTelephone()
        elif choice == 2:
            searchFname()
        elif choice == 3:
            searchLname()
        elif choice == 4:
            searchArea()
        elif choice == 5:
            break
        else:
            print('Invalid choice')

def searchTelephone():
    con=sql.connect(host='localhost', user='root', passwd='root', db='test')
    
    if not con.is_connected():
        print('Connection failed')
        return
    
    cursor=con.cursor()
    
    print('Search Contact Number')
    print('=====================')
    
    tel=int(input('Enter Contact Number: '))

    query="SELECT * FROM contacts WHERE telephone={}".format(tel)
    cursor.execute(query)

    resultSet = cursor.fetchone()
    
    if cursor.rowcount == 0:
        print("Sorry! Record not found")
        input("Press any key to continue...")
        con.close()
        return
    
    for field in resultSet:
        print(field, end=' ')
        
    input('\n\nPress any key to continue...')

    con.close()    

def searchFname():
    con=sql.connect(host='localhost', user='root', passwd='root', db='test')
    
    if not con.is_connected():
        print('Connection failed')
        return
    
    cursor=con.cursor()
    
    print('Search First Name')
    print('=================')
    
    fname=input('Enter First Name: ')
    fname=fname.upper()
    
    query="SELECT * FROM contacts WHERE fname='{}'".format(fname)
    
    cursor.execute(query)

    resultSet = cursor.fetchall()
    
    if cursor.rowcount == 0:
        print("Sorry! Record not found")
        input("Press any key to continue...")
        con.close()
        return

    for record in resultSet:
        for field in record:
            print(field, end=' ')
        print()
        
    input('Press any key to continue...')

    con.close()    

def searchLname():
    con=sql.connect(host='localhost', user='root', passwd='root', db='test')
    
    if not con.is_connected():
        print('Connection failed')
        return
    
    cursor=con.cursor()
    
    print('Search Last Name')
    print('================')
    
    lname=input('Enter Last Name: ')
    lname=lname.upper()
    
    query="SELECT * FROM contacts WHERE lname='{}'".format(lname)
    
    cursor.execute(query)

    resultSet = cursor.fetchall()
    
    if cursor.rowcount == 0:
        print("Sorry! Record not found")
        input("Press any key to continue...")
        con.close()
        return

    for record in resultSet:
        for field in record:
            print(field, end=' ')
        print()
        
    input('\nPress any key to continue...')

    con.close()    

def searchArea():
    con=sql.connect(host='localhost', user='root', passwd='root', db='test')
    
    if not con.is_connected():
        print('Connection failed')
        return
    
    cursor=con.cursor()
    
    print('Search Area')
    print('===========')
    
    area=input('Enter Area: ')
    area=area.upper()

    query="SELECT * FROM contacts WHERE area='{}'".format(area)
    
    cursor.execute(query)

    resultSet = cursor.fetchall()
    
    if cursor.rowcount == 0:
        print("Sorry! Record not found")
        input("Press any key to continue...")
        con.close()
        return

    for record in resultSet:
        for field in record:
            print(field, end=' ')
        print()
        
    input('\nPress any key to continue...')

    con.close()    

#  __main__ module

menu()
