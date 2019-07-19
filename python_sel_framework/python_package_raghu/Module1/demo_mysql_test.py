import mysql.connector 

mySQLconnection = mysql.connector.connect(user='devel', password='withc--',
                              host='mysqldev.avangate.local',
                              database='avangate')

sql_select_Query = "select * from sales where idsale IN (68945229, 68945228)"
cursor = mySQLconnection .cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
print("Total number of rows: ", cursor.rowcount)
for row in records:
       print("IdSale = ", row[0], )
       print("IdAccount = ", row[1])
       print("RefNo  = ", row[3])
       print("ExternalRefNo  = ", row[7], "\n")
cursor.close()

mySQLconnection.close()

print(mySQLconnection)

