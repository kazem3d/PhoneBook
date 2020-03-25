#reading excel file <list.xls> and create database with it

import sqlite3
import xlrd



address="list.xls"
#address=input('Enter file path :')

tabel_list=[]

#connecting to excel sheet 

excel_reader=xlrd.open_workbook(address) 
sheet = excel_reader.sheet_by_index(0) 
sheet.cell_value(0,0) 

#fill a list of list with excel content
for i in range(2,sheet.nrows):
    
    row=sheet.row_values(i)  
    tabel_list.append(row)  
    

#created database with tabel
conn=sqlite3.connect("DataBase")
curser=conn.cursor()

curser.execute('''CREATE TABLE IF NOT EXISTS phonebook (
    
    id integer PRIMARY KEY,
    name TEXT   ,
    job TEXT ,
    internal integer NULL,
    direct integer NULL,
    fax integer NULL,
    IpPhone integer NULL
    )''')

#fill database tabel with content of list
        
for i in tabel_list:
    name=i 
    curser.execute('INSERT INTO phonebook (name,job,internal,direct,fax,IpPhone)  VALUES (?,?,?,?,?,?)' 
    ,(i)
    )

conn.commit()