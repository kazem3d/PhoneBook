#using excel file insted of sql database
import xlrd

address="list.xls"
tabel_list=[]

excel_reader=xlrd.open_workbook(address) 
sheet = excel_reader.sheet_by_index(0) 
sheet.cell_value(0,0) 

for i in range(2,sheet.nrows):
    
    row=sheet.row_values(i)  
    tabel_list.append(row)   

    



