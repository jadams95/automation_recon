import os

ip = ""

# You call IP address twice Need to Fix
# Frowned upon using global variables
# Plan to use argparse

def automation(ip):
    """ Receives the ip address and commands, and then does the recon to an output file """
    commands = ['nmap.exe -sT -p- -oN c:\\BugBounty\\test3.txt ',
    r'C:\nikto\nikto.bat -output C:\\BugBounty\\test3.txt -host ']
    for command in commands:
        os.system(command + ip)
    
    
    
automation("216.18.168.66")