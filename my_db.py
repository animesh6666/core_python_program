import mysql.connector as sqlc

conn = sqlc.connect(host='localhost', user = 'root', passwd = '',database ='student')

mycursor = conn.cursor()
try:
    mycursor.execute("CREATE DATABASE student")
except:
    pass

try:
    mycursor.execute("CREATE TABLE students(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20),addr VARCHAR(150),age INT)")
except:
    pass

def add_data():
    try:
        sql = "INSERT INTO students VALUES(%s,%s,%s,%s)"
        info = [input("Enter id number : "),
                input("Enter Name : "),
                input("Enter City Name : "),
                input("Enter Age : ")]

        mycursor.execute(sql,info)

        conn.commit()

    except :
        print("You enter same id.")


def delete_data(i):
    try :
        sql ="DELETE FROM students WHERE id = %s "
        delete = [i]
        mycursor.execute(sql,delete)
        conn.commit()
    except (i!= "SELECT id FROM students ") :
        print("You enter invalid id number.")

def eddit_data(i):
    try :
        print("Please select field of update.")
        print("""A. Name
                B.  Address
                C. Age""")
        option = input("Enter Field number : ")

        if (option == 'A'):
            sql = "UPDATE students SET name = %s WHERE id = %s "
            update = [input("Enter New Name: "),i]
            mycursor.execute(sql,update)
            conn.commit()
        
        elif (option == 'B'):
            sql = "UPDATE students SET addr = %s WHERE id = %s "
            update = [input("Enter New ADDRESS: "),i]
            mycursor.execute(sql,update)
            conn.commit()
        
        elif(option == 'C'):
            sql = "UPDATE students SET age = %s WHERE id = %s "
            update = [input("Enter New Age: "),i]
            mycursor.execute(sql,update)
            conn.commit()
        else :
            print("Please Select valid ID number.")
    except :
        print('Enter valid ID number.')

def find_data():
    print("Please select Field of Filter data.")
    print("""A. ID
            B. NAME
            C. ADDRESS
            D. AGE""")
    
    option = input("Enter your Filter Option : ")

    if (option == 'A'):
        sql = "SELECT * FROM students WHERE id = %s"
        update =[int(input("Enter id number : "))]
        mycursor.execute(sql,update)
        data = mycursor.fetchall()
        print(data)

    elif(option == 'B'):
        sql = "SELECT * FROM students WHERE name = %s"
        update =[input("Enter NAME : ")]
        mycursor.execute(sql,update)
        data = mycursor.fetchall()
        print(data)
       
    elif(option == 'C'):
        sql = "SELECT * FROM students WHERE addr = %s"
        update =[input("Enter ADDRESS : ")]
        mycursor.execute(sql,update)
        data = mycursor.fetchall()
        print(data)

    elif(option == 'D'):
        sql = "SELECT * FROM students WHERE age = %s"
        update =[input("Enter AGE : ")]
        mycursor.execute(sql,update)
        data = mycursor.fetchall()
        print(data)

    else :
        print("ENTER VALID OPTION.")

def privew_data():
    sql = "SELECT * FROM students"
    mycursor.execute(sql)
    data = mycursor.fetchall()

    for i in data:
        print(i)



print("Select option of bellow : ")
print("""1. Add data
        2. Remove data
        3. Eddit data
        4. Find data
        5. preview """)

option = int(input("Select your option : "))
if (option == 1) :
    add_data()
    add = bool(input("You like to add more data :"))

    if (add == 'yes'):
        number = int(input("Hoe many more data you like to input : "))
        for i in range(number):
            add_data()
        print('Thank you for entry.')

    else:
        print('Thank you for entry.')
elif(option == 2):
    i = int(input("Enter id number of deliting data : "))
    delete_data(i)

elif(option == 3):
    i = int(input("Enter id number of Updateing data : "))
    eddit_data(i)

elif(option == 4):
    find_data()

elif(option == 5):
    privew_data()