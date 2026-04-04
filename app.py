#import with password and database is not viewable on github 
#show table on python. retrieve from db
#show attribute from table employees
mycursor = projectDB.cursor(buffered=True)

mycursor.execute("SELECT age FROM employees")

myresult = mycursor.fetchone()

for row in myresult:
    print(row)
