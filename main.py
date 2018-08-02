import os
from packages.main_functions import ping_cmd
from packages.Classes import ImportGsheet

gsheet = ImportGsheet()

# Print the list of Worksheets/Customers
print("""Available Customers on the Google Sheet are:
=====================================""")
print(gsheet.getSpreadsheet().title)
print("=====================================")
for num, sheet in enumerate(gsheet.getcustomer_list()):
    print(num, sheet.title)

# Get input from Keyboard to access specific Worksheet
choice = int(input("Type the customer name to display their devices: "))

# Run through the worksheets/customers and check for error correction ** To be improved.
while choice > len(gsheet.getcustomer_list()):
    print("Invalid Selection! \n Try again?")
    choice = int(input("Type the customer name to display their devices: "))

else:
    for num, sheet in enumerate(gsheet.getcustomer_list()):
        if choice == num:

            # Variables for Current Customer for easier reference
            selected_customer = gsheet.getcustomer(choice)
            list_of_devices = gsheet.getdevice_list(choice)

            # Show Customer name and devices
            print("####################")
            print(selected_customer.title)
            print("####################")

            # for each item under customer print
            for num, devices in enumerate(list_of_devices):
                print(num, '\t',  devices[0] + "\t" + devices[1])

            # Select the name of the device to ping from Keyboard
            selected_device = int(input("Select device to ping: "))

            # Ping test
            while selected_device > len(selected_customer.col_values(1)):
                print("Invalid Selection ", selected_device)
                print("Try again:")
                device = int(input("Select device to ping: "))

            else:
                for num, elements in enumerate(list_of_devices):
                    if selected_device == num:
                        print(selected_customer.title)
                        print("Pinging " + elements[0])
                        response = os.system('ping -c 3 ' + elements[1])
                        if response == 0:
                            print("=========\nResult\n=========")
                            print(selected_customer.title, elements[0], 'is up!')
                        else:
                            print(selected_customer.title, elements[0], 'is down!')