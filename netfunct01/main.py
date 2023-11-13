#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import crayons
import json
from time import sleep


# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') # fstring
        sleep(1)
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'{crayons.green("Attempting to sending command")} --> {mycmds}')
            sleep(1)
            # we'll learn to write code that sends cmds to device here
    return None


# function to reboot
def devicereboot(devicecmd):

    for ip in devicecmd.keys():
        print(f'Connecting to {ip}')
        sleep(2)
        print(f'REBOOTING NOW!')
        sleep(1)
    return None

# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    #devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    #["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}
    with open("devicecmd.json", "r") as devicecmdfile:
        devicecmd = json.load(devicecmdfile) #decode the JSON from the file to pythonic data


    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices
    sleep(3)
    devicereboot(devicecmd) # call function to reboot device

# call our main function
main()

