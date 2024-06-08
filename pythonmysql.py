import mysql.connector

mydb = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '',
    database= 'python'
)

'''if mydb :
    print('connected to mysql')
else :
    print('Not connected')
'''

mycursor = mydb.cursor()

# sql = 'insert into student values(1, "Ram", "Male")'
# mycursor.execute(sql)
# mydb.commit()

sql1 = 'delete from student'
mycursor.execute(sql1)
mydb.commit()

# result = mycursor.fetchall()
# for x in result :
#     print(x)

