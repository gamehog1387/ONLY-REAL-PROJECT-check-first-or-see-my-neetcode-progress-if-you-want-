#import with password and database is not viewable on github 
#show table on python. retrieve from db

mycursor = projectDB.cursor(buffered=True)

mycursor.execute("SELECT * FROM employees")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)
