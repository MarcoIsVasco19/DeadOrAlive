import os
import subprocess
from subprocess import PIPE
from packages.Classes import ImportGsheet

customer = ImportGsheet()

# Unused
def pingDevices(ssh_args):
    """

    :param ssh_args:
    :return ping Results:
    """
    proc = subprocess.Popen(ssh_args, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)

    result_output = proc.stdout.readlines()
    result_error = proc.stderr.readlines()

    if result_output == []:
        print(result_error)
    else:
        for line in result_output:
            print(line)


def ping_cmd(wks_name, device):

    for num, elements in enumerate(customer.getdevice_list(wks_name)):
        if device == num:
            # print(customer.getcustomer().title)
            print("Pinging " + elements[0])
            response = os.system('ping -c 3 ' + elements[1])
            if response == 0:
                print("=========\nResult\n=========")
                return elements[0], 'is up!'
            else:
                return device[0], 'is down!'