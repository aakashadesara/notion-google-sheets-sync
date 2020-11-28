## 📊 Notion x Google Sheets
This is a quick utlity to sync a Google Sheet with a Notion Collection. I primarily made it to automate some workflows for [The Daily Dropout](http://dailydropout.fyi/) but thought it might be useful for other folks who use Notion + Sheets as part of their work tools.

![Demo Notion Google Sheets Sync](/demo.png)

### How to Use Notion x Google Sync
0. Make sure you have Python3 installed and use Python3 / Pip3 to install these packages:
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib      
pip install notion   
```

1. Replace `<YOUR_SPREADSHEET_ID>` in `sync.py` with your Google Sheets Spreadsheet ID. In my case, the link was `https://docs.google.com/spreadsheets/d/1-bj7rMv_TIC6IrwhsMcxVv6FJLVRv6jk6gjBWy7pNbQ/edit#gid=0` so I took everything after the `/d/` and that was my Spreadsheet ID.

2. Go through [these steps](https://developers.google.com/sheets/api/quickstart/python) set up by Google to let you use the Google Sheets API.

3. Query the cells you want using Google Sheets syntax (ex. `Sheet1!A1:AA`) and replace `<YOUR_SPREADSHEET_SELECTION>` in the code with that query.

4. Get your Notion V2 Token by visiting your Notion page from a browser and copy the token_v2 Cookie. Replace `<YOUR_NOTION_TOKEN_V2>` with the cookie.

5. Make a new Notion page with a single Block (a Collection block) and copy your Notion page link and replace `<YOUR_NOTION_PAGE_LINK>` with the link. The Notion page you made should look like this:

![Empty Page](/empty_page.png)


6. And you should be good to go! Now just run `python sync.py` and everything should work.


### Work In Progress
_This is in order of priority_
- [ ] Typing for Collection properties (so it's not just text)
- [ ] better reloading (instead of deleting + re-populating Collection)
- [ ] Chron job to automatically sync on a cadence
- [ ] onChangeListener for Google Sheet (so users can toggle between Chron job and auto-sync)

If you want to help, feel free to fork + make a pull request. Contact me on Twitter [@aakashadesara](https://twitter.com/aakashadesara) before you work on something big so we do not have multiple people working on the same changes.

### Thanks
Special thanks to the folks working on the [Notion Python API](https://github.com/jamalex/notion-py)
