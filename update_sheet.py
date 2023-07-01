import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the Google Sheet ID and the name of the sheet you want to update
spreadsheet_id = '1cRPN6rl55R8WerMHN28qtz0nMM8c_L10Xa14srtAqPM'
sheet_name = 'Current Month'

# Define the path to your service account credentials JSON file
credentials_file = 'runclub-338918-88f1e2ad86c6.json'

# Authorize and authenticate with Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open_by_key(spreadsheet_id)

# Get the specific sheet by name
worksheet = sheet.worksheet(sheet_name)

# Read the local CSV file
csv_file = 'googleData.csv'
with open(csv_file, 'r') as file:
    csv_data = file.read()

# Update the sheet with CSV data
worksheet.update('A1', csv_data)

print('Google Sheet updated successfully.')