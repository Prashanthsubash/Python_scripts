import mysql.connector

my_db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Aspire@123",
    database = "assignments")

print(my_db)

mycursor = my_db.cursor()


sql = ("INSERT INTO employees (emp_id, emp_name, dob, doj, sex, phn, salary, Dept_id) " 
       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
values = (115,"Umar", "1992-07-08", "2013-10-09","F","67838653",4550.50,16)

mycursor.execute(sql, values)
my_db.commit()

print(mycursor.rowcount," record(s) inserted")
print(my_db)

mycursor.execute("select * from employees")
for data in mycursor:
    print (data)
