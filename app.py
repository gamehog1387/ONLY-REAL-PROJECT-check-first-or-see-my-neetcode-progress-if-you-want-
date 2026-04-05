
#show
mycursor = projectDB.cursor(buffered=True)


with open('employees.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        sql = "INSERT INTO employees (employee, age, pay, dept_code, skill_level) VALUES (%s, %s, %s, %s, %s)" 
        mycursor.execute(sql, row)
        

projectDB.commit()

# INSERT CSV FILE INTO employees
