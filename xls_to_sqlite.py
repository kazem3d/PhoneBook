import sqlite3
import xlrd

address="list.xls"
#address=input('Enter file path :')

tabel_list=[]

excel_reader=xlrd.open_workbook(address) 
sheet = excel_reader.sheet_by_index(0) 
sheet.cell_value(0,0) 

for i in range(2,sheet.nrows):
    
    row=sheet.row_values(i)  
    tabel_list.append(row)  
    

conn=sqlite3.connect("DataBase")
curser=conn.cursor()

curser.execute('''CREATE TABLE IF NOT EXISTS phonebook (
    
    id integer PRIMARY KEY,
    name TEXT   ,
    job TEXT ,
    internal TEXT ,
    direct TEXT,
    fax TEXT NULL,
    IpPhone TEXT NULL
    )''')

        
for i in tabel_list:
    name=i 
    curser.execute('INSERT INTO phonebook (name,job,internal,direct,fax,IpPhone)  VALUES (?,?,?,?,?,?)' 
    ,(i)
    )

conn.commit()