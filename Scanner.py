#import some stuff

import base64
import sys
import argparse

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
     ###                @Luke__Ager               ###
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

#Checks if input is correct and help file
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='my program help')
    parser.add_argument('-f', help='specify macro file path', required=True)
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
        print "File Accepted - Performing Validation Checks"





