Built with Python version 3.6 (supported from version 3.4.x)

Python Modules
------------------

third party Packages Required
-----------------
oauth2client
gspread

How to install
----------------
pip install {module}

Program contents:

code --> packages
                   --> __init__.py
                   --> main_classes.py
                   --> main_functions.py
     --> app.py
     --> README.md (This file)


-------------------------


Proposed Program Logic

API Script (pulling info from google sheets, customer info) Integration done
|
--> Build Customer List Classes.py
  |
  --> From there we can import an instace of the sheet. (May need to add more variables to cater for more Sheets/Teams)
    |
    --> This instance will have all information in the Google Spreadsheet specified by the URL. Just a matter of using the correct          gspread (module) methods.

To be continued...

-------------------------



