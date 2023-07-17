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
    csv_data = file.readlines()

# Parse CSV data into a 2D list and remove leading/trailing whitespace
csv_data = [row.strip().split(',') for row in csv_data]

# Create a new 2D list with numerical values as numbers (without leading "'")
csv_data_numeric = [[float(cell) if cell.isnumeric() else cell for cell in row] for row in csv_data]

# Get the range of cells to update
start_cell = 'A1'
end_cell = chr(ord('A') + len(csv_data_numeric[0]) - 1) + str(len(csv_data_numeric))

# Update the sheet with CSV data as numbers
worksheet.update_cells(worksheet.range(f'{start_cell}:{end_cell}'), csv_data_numeric, value_input_option='USER_ENTERED')

print('Google Sheet updated successfully.')