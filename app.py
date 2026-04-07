mycursor = projectDB.cursor(buffered=True)

mycursor.execute("SELECT * FROM projects")

myresult = mycursor.fetchall()
with open('projects.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        sql = "INSERT INTO projects (project, dept_helping, successful_proj, percent_done, completed_projects, customer_names ) VALUES (%s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, row )

    for row in myresult:
        print(row)
projectDB.commit()
