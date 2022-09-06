import boto3
'''import  MySQLdb
mydb = MySQLdb.connect(host="localhost", user="root",password="root@123",database="employee")
mycursor=mydb.cursor()

#sql = "INSERT INTO employee (id, name, basic, hra) VALUES (%s, %s, %s, %s)"
#val = ("22866", "rohith", "30000","10000")
mycursor.execute("SELECT *, basic+hra as salary FROM employee")
myresult = mycursor.fetchall()



print("ID | NAME | BASIC | HRA | salary")
for x in myresult:
    print(x[0], x[1], x[2], x[3], x[4])
#mydb.commit()
#print(mycursor.rowcount, "record inserted.")'''