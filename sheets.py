### https://developers.google.com/sheets/api/quickstart/python

import traceback
import gspread
from google.oauth2 import service_account

import config

sheetName = "Test1"
space = '!A:J'
sheet_id = "1dzC63bulx_j1d-aTuFjH-jhDM5hr8LISQqzPovFku54"
#https://docs.google.com/spreadsheets/d/1dzC63bulx_j1d-aTuFjH-jhDM5hr8LISQqzPovFku54/edit#gid=0

# Creates and returns a google sheets client.
##############################################
def get_google_sheets_client():
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    GPC_CREDENTIALS = service_account.Credentials.from_service_account_info(config.sheets_credentials , scopes=scopes)

    gc = gspread.authorize(GPC_CREDENTIALS)
    return gc

# Extract google_sheets spam users.
###################################
def clear_google_sheets_values(sh):
    print(sh.values_clear(sheetName+space)) # Clear Cells populated by process.

def update_data_to_sheets(data=None, cust_space=None):
    if data==None:
        data = {'values': [[i+j for j in range(10)] for i in range(10)]}
        
    if cust_space==None:
        cust_space = space
    
    # Get the Google Client for the update
    gc = get_google_sheets_client()

    # Open Google Sheet
    sh = gc.open_by_key(sheet_id) 

    # Clear all data for range
    clear_google_sheets_values(sh)

        # Send the update API call
    print(sh.values_update(range=sheetName+cust_space,
                        params={
                            'valueInputOption': 'RAW'
                        },body=data))

if __name__ == '__main__':
    try: 
        update_data_to_sheets()
        
    except Exception as e:
        traceback.print_exc()