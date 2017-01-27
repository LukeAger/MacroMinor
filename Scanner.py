#import some stuff

import argparse
import sys
import time
import os
import inspect
import base64
from Modules import QuestionmMod


cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"subfolder")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)


#set and print banner in longstring variable
banner = """\n
     ################################################
     ################################################
     ###   ___  ___  ___   _____ ______  _____    ###
     ###   |  \/  | / _ \ /  __ \| ___ \|  _  |   ###
     ###   | .  . |/ /_\ \| /  \/| |_/ /| | | |   ###
     ###   | |\/| ||  _  || |    |    / | | | |   ###
     ###   | |  | || | | || \__/\| |\ \ \ \_/ /   ###
     ###   \_|  |_/\_| |_/ \____/\_| \_| \___/    ###
     ###                                          ###
     ###   ___  ___ _____  _   _  _____ ______    ###
     ###   |  \/  ||_   _|| \ | ||  _  || ___ \   ###
     ###   | .  . |  | |  |  \| || | | || |_/ /   ###
     ###   | |\/| |  | |  | . ` || | | ||    /    ###
     ###   | |  | | _| |_ | |\  |\ \_/ /| |\ \    ###
     ###   \_|  |_/ \___/ \_| \_/ \___/ \_| \_|   ###
     ###                                          ###
     ###   Twitter: @Luke__Ager     Versoin 0.1   ###
     ###  Still in development: Not safe for use  ###
     ###                                          ###
     ################################################
     ################################################
"""
print banner

##################################################################
##################################################################
#########################LOGIC LIVES HERE#########################
##################################################################
##################################################################

exit = "Exiting:                             - No Variables To Scan Or File Could Be Clear Text"

#Checks if input is correct and help file
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example: Scanner.py -f targetfile.txt')
    parser.add_argument('-f', metavar='FILENAME', help='specify macro file path', required=True)
    args = parser.parse_args()
#Checks if imported or run directly
else:
    print "This script does not like to be imported right now"
#Sets input file to the value of ifile
with open(sys.argv[2], 'r') as f:
    ifile = f.read()
    if len(sys.argv) == 1:
        empty = "I don't know how you got here but please give me something to scan!"
        print empty
    else:
        time.sleep(1)
        print "File Located Successfully            - Performing Validation Checks"
        time.sleep(1)
#Validation checks
if len(ifile) == 0:
    print "Validation Failed                    - File Is Empty: Check File"
else:
    print "Validation Check 1:                  - Success"
    time.sleep(1)
if "= " not in ifile:
    print "Validation Check 2:                  - No Variables Detected"
    time.sleep(1)
    answer = QuestionmMod.query_yes_no("Do You Want To Check For base64 Encoding?....WARNING non base64 will cause exit")
    if answer == "yes":
        time.sleep(1)
#Encoding functions required here
        print "Checking Encoding"
        time.sleep(1)
        print "Checking For base64"
        bcheck = len(ifile) % 3
        if bcheck == "0":
            print exit
        else:
            time.sleep(1)
            print "Check Complete:                      - File Is Base64"
            var1 = base64.b64decode(ifile)
            time.sleep(1)
            print "Check Complete:                      - Possible Base64 Detected"
            time.sleep(1)
            print "Decoding Complete                    - Scanning For Variables"
            if "= " not in var1:
                print "Validation Failed:                  - No Encoding Or Variables Detected"
            else:
                print "Possible Variables Detected          - Continuing Scan"
                print var1
    else:
        time.sleep(1)
        print "Validation Check 3:                  - Failed: Nothing To Scan"
        print exit
        time.sleep(1)
else:
    print "Validation Check 2:                  - Success"
    time.sleep(1)
    print "Validation Checks Complete"
    time.sleep(1)










