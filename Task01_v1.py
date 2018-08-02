import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Scope used for the Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/spreadsheets.readonly']

# Credentials used to authenticate to the Google Sheet
credentials = ServiceAccountCredentials.from_json_keyfile_name('./keyStore/SpreadSheets-eae997fe25bf.json', scope)

# Authorize the Spreadsheet
gc = gspread.authorize(credentials)

# Define the spreadsheet to be used in the script.
spreadsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1DkEi4DtUddq4BKIAJjna41toPhX8UKQSEs9-MxZinUM/edit#gid=0')

# Declare the list of all Worksheets
worksheet_list = spreadsheet.worksheets()

# Print the list of Worksheets/Customers
print("""Available Customers on the Google Sheet are:
=====================================""")
print(spreadsheet.title)
print("=====================================")
for num, sheet in enumerate(worksheet_list):
    print(num, sheet.title)

# Get input from Keyboard to access specific Worksheet
choice = int(input("Type the customer name to display their devices: "))

# Run through the worksheets to pull the wks specified from the keyboard
while choice > len(worksheet_list):
    print("Invalid Selection! \n Try again?")
    choice = int(input("Type the customer name to display their devices: "))

else:
    for num, sheet in enumerate(worksheet_list):
        if choice == num:
            # create variable for worksheet
            wks = spreadsheet.get_worksheet(choice)

            # Output Whole Worksheet as string
            list_of_devices = wks.get_all_values()

            # Show Customer name and devices
            print("####################")
            print(wks.title)
            print("####################")

            # for each item under customer print
            for num, devices in enumerate(list_of_devices):
                print(num, '\t',  devices[0] + "\t" + devices[1])

            # Select the name of the device to ping from Keyboard
            device = int(input("Select device to ping: "))

            # Ping test
            while device > len(wks.col_values(1)):
                print("Invalid Selection ", device)
                print("Try again:")
                device = int(input("Select device to ping: "))

            else:
                for num, elements in enumerate(list_of_devices):
                    if device == num:
                        print(wks.title)
                        print("Pinging " + elements[0])
                        response = os.system('ping -c 3 ' + elements[1])
                        if response == 0:
                            print("=========\nResult\n=========")
                            print(elements[0], 'is up!')
                        else:
                            print(elements[0], 'is down!')