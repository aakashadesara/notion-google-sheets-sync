from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from notionpy.notion.client import NotionClient

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# start - CHANGE THESE
SAMPLE_SPREADSHEET_ID = '<YOUR_SPREADSHEET_ID>' 
SAMPLE_RANGE_NAME = '<YOUR_SPREADSHEET_SELECTION>'
NOTION_V2_TOKEN = "<YOUR_NOTION_TOKEN_V2>" 
NOTION_PAGE_LINK = "<YOUR_NOTION_PAGE_LINK>"
# end   - CHANGE THESE

def get_sheet():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
        return None
    else:
        print('%s rows found.' % len(values))
        return values

def get_prop_type(data):
    # todo parse data to support types

    return 'text'

def notion_update(data):
    client = NotionClient(token_v2=NOTION_V2_TOKEN)
    
    block = client.get_block(NOTION_PAGE_LINK)
    cv = block.collection
    rows = cv.get_rows()

    cv.clear_properties()
    for row in rows:
        row.remove()


    title = data[0][0]
    cv.set_property('title', title, slug=title, property_type='title')
    for i, prop in enumerate(data[0][1:]):
        prop_type = get_prop_type(data[1][1:][i]) if data[1] and data[1][1:] else 'text'
        cv.set_property(prop, prop, slug=prop, property_type=prop_type)

    for row in data[1:]:
        new_row = cv.add_row()
        for i, value in enumerate(row):
            prop = data[0][i]
            new_row.set_property(prop, value)

if __name__ == '__main__':
    data = get_sheet()
    notion_update(data)
