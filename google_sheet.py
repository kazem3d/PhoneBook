import gspread 
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds=ServiceAccountCredentials.from_json_keyfile_name('t.json',scope)
client=gspread.authorize(creds)

sheet=client.open('test1').sheet1

# p=sheet.get_all_records()
# print (p)

# sheet.update('B4', "it's down there somewhere, let me take another look.")
# sheet.append_row(['کاظم قناتی'])