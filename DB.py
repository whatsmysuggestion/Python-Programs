import mysql.connector
#127.0.0.1   or local ipaddress or localhost
conn = mysql.connector.connect(host='localhost',
                               port=3306,user='root',passwd='root',db='viral')
cursor = conn.cursor()

sql = "SELECT * FROM EMPLOYEE"

try:

    cursor.execute(sql)
    results = cursor.fetchall()

    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]

        print("fname = %s,lname = %s,age = %d,sex = %s,income = %d" %(fname, lname, age, sex, income))

except:

    conn.rollback()

conn.close()