mycursor = projectDB.cursor(buffered="True")

mycursor.execute("SELECT * FROM customer_list")

myresult = mycursor.fetchall()
with open('customer_list.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        sql = "INSERT INTO customer_list (customer, contracts_done, VALUE, MONEY_MADE, complaints) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(sql, row )

    for row in myresult:
        print(row)
projectDB.commit()
