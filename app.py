

#import with password and database is not viewable on github 

mycursor = projectDB.cursor(buffered=True)

mycursor.execute("CREATE TABLE IF NOT EXISTS employees (employee VARCHAR (50), age INT, pay INT)")

mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)
#make a exectuable for info into table employees
sqlFormula = "INSERT INTO employees (employee, age, pay) VALUES (%s, %s, %s)"
employees = [("Sarah", 22, 15),
            ("Michelle", 22, 15),
            ("Tyler", 22, 15),
            ("Harold", 22, 15),
            ("SANDEEEEE", 22, 15),]


mycursor.executemany(sqlFormula, employees)
projectDB.commit()

print("Record inserted successfully")
