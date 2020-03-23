import sqlite3

conn=sqlite3.connect("DataBase")
curser=conn.cursor()

tabel_list=[]

curser.execute('SELECT name,job,internal,direct,fax,IpPhone FROM phonebook')
rows=curser.fetchall()
for row in rows:
    tabel_list.append(row)  

