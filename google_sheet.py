import gspread 
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

try:

    creds=ServiceAccountCredentials.from_json_keyfile_name('t.json',scope)
    client=gspread.authorize(creds)

    sheet=client.open('phonebook').sheet1
    sheet_request=client.open('phonebook').get_worksheet(1)

except:
    print('server not found')
    connect_message='خطا در ارتباط با سرور'
else:
    print('server connected')
    connect_message='ارتباط با سرور برقرار است'


def fetch_data():
    p=sheet.get_all_values()
    return p

# sheet.update('B4', "it's down there somewhere, let me take another look.")
# sheet.append_row(['کاظم قناتی'])