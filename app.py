#show data for departments
mycursor = projectDB.cursor(buffered=True)

mycursor.execute("SELECT * FROM departments")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)
