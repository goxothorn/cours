import sqlite3, os, time, time_perso, json, requests
import pandas
conn = sqlite3.connect("testdb4.db")
conn.close()

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTEGER
)
""")
conn.commit()

users = []
users.append(("olivier", 30))
users.append(("jean-louis", 90))
cursor.executemany("""
INSERT INTO users(name, age) VALUES(?, ?)""", users)

conn.execute("""SELECT id, name, age FROM users""")
user1= cursor.fetchone()
print (user1)

cursor.execute("""
INSERT INTO users(name, age) VALUES(?, ?)""", ("olivier", 30))

cursor.execute("""SELECT id, name, age FROM users""")
rows = cursor.fetchall()
for row in rows:
    print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))

print (rows)

df = pandas.read_csv("TestOlv.csv")
df.to_sql("audience", conn, if_exists = "append", index = False)

cursor.execute("""SELECT name, SUM (age) 
FROM users
GROUP BY name""")
test01= cursor.fetchall()
print(test01)
cursor.execute("""SELECT day FROM audience""")
us= cursor.fetchmany(2)
print(us)

id = 2
cursor.execute("""SELECT id, name FROM users WHERE id=?""", (id,))
response = cursor.fetchone()
print (response)

t = cursor.execute("""SELECT * FROM audience""")
rows2 = t.fetchone()
print (rows2)

t.description
a= cursor.execute("""SELECT hour FROM audience""")

cursor.execute("""SELECT * FROM audience0""")
test = cursor.fetchall()
test[5]


conn = sqlite3.connect("testdb7.db")
conn.close()

data5 = pandas.read_csv("Test4.csv", header= 0, sep=",")
data3 = pandas.read_csv("Test10.csv", header=0, sep = ",")
data5.to_sql("audience2", conn, if_exists = "replace", index = False)
data3.to_sql("audience01", conn, if_exists= "replace", index= False)
conn.commit()
cursor = conn.cursor()
data3.to_sql("audience0", conn, if_exists= "replace", index= False)

cursor.execute("""SELECT * FROM audience0 UNION SELECT * FROM audience2""")
test = cursor.fetchall()
len(test)
conn.commit()
test
print(test)




cursor.execute("""SELECT * FROM audience2""")
cursor.description

cursor.execute("""SELECT day, SUM(imps_matched) FROM audience01 GROUP BY seller_member_name""")
t = cursor.execute("""SELECT seller_member_name, SUM(imps_matched) FROM audience0 """)
cursor.execute("""SELECT day, SUM(imps_matched) FROM audience01 GROUP BY day""")
t = cursor.execute("""SELECT day FROM audience01""")

cursor.execute("""SELECT * FROM audience0 LEFT JOIN audience2 ON audience0.hour = audience2.hour WHERE audience2.hour IS NULL""")
t = cursor.execute("""SELECT * FROM audience0 EXCEPT SELECT * FROM audience2""")
t.description


cursor.execute("""INSERT * INTO audience2 VALUES ("%s", "%s", "%s", "%s")""", """SELECT * FROM audience0 EXCEPT SELECT * FROM audience2""" )
cursor.execute("""INSERT * INTO audience2 VALUES ("%s", "%s", "%s", "%s")""", test[i] )

cursor.execute("""INSERT INTO audience2  SELECT * FROM audience0 EXCEPT SELECT * FROM audience2""" )


datatest =  pandas.read_csv("test09.csv", header = 0, sep = "\t")
datatest
