mycursor = projectDB.cursor(buffered=True)

mycursor.execute(""" CREATE TABLE IF NOT EXISTS departments (department VARCHAR (50), ID INT, clearance INT, pay_avg INT)""")

mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)
    #INFO FOR deparments info in departments table
sqlFormula = "INSERT INTO departments (department, ID, clearance, pay_avg) VALUES (%s, %s, %s, %s)"
departments = [("cyber", 3104, 1, 34),
               ("DEV OPS", 4942, 2, 53),
               ('software', 5932, 2, 60), 
               ("cyber", 3104, 4, 43),
               ("front end", 4942, 2, 24),
               ('database', 5932, 4, 60),
               ("IT", 3104, 2, 34),
               ("Help Desk", 4942, 1, 25),
               ('HR', 5932, 4, 60),]

mycursor.executemany(sqlFormula, departments)

projectDB.commit()
