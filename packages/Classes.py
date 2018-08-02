import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class ImportGsheet:

    def getSpreadsheet(self):
        """
        Author : Marco Marques
        Contributors: Anton Smit,

        Function connects to google sheets, retrieves customer info to be used later in main()

        :return list Customers:
        """

        # Scope used for the Sheets
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive',
                 'https://www.googleapis.com/auth/spreadsheets.readonly']

        # Credentials used to authenticate to the Google Sheet
        credentials = ServiceAccountCredentials.from_json_keyfile_name('./keyStore/SpreadSheets-eae997fe25bf.json', scope)

        # Authorize the Spreedsheet
        gc = gspread.authorize(credentials)

        # Define the spreadsheet to be used in the script.
        spreadsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1DkEi4DtUddq4BKIAJjna41toPhX8UKQSEs9-MxZinUM/edit#gid=0')

        return spreadsheet

    def getcustomer_list(self):
        wks = self.getSpreadsheet()
        return wks.worksheets()

    def getcustomer(self, worksheet_title):
        wks = self.getSpreadsheet()
        return wks.get_worksheet(worksheet_title)

    def getdevice_list(self, customer):
        wks = self.getSpreadsheet()
        return wks.get_worksheet(customer).get_all_values()