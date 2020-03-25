import sqlite3

#connect to database 
conn=sqlite3.connect("DataBase")
curser=conn.cursor()



#fill a list of list with database tabel content
def get_from_database():
    tabel_list=[]
    curser.execute('SELECT name,job,internal,direct,fax,IpPhone FROM phonebook')
    rows=curser.fetchall()
    for row in rows:
        tabel_list.append(row)  
    return tabel_list

#fill database with a list of list : <tabel_list>
def fill_database(tabel_list):
    for i in tabel_list:
        
        curser.execute('INSERT INTO phonebook (name,job,internal,direct,fax,IpPhone)  VALUES (?,?,?,?,?,?)' 
        ,(i)
        )

    conn.commit()



#clear database before updating
def clear_tabel():
    conn=sqlite3.connect("DataBase")
    curser=conn.cursor()
    curser.execute('DELETE FROM phonebook;')
    conn.commit()
    print('tabel clear')

    
def update_tabel():
    
    
    print('tabel_updated')
  