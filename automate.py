import os

ip = ""

# You call IP address twice Need to Fix
# Frowned upon using global variables
# Plan to use argparse

def automation(ip):
    """ Receives the ip address and commands, and then does the recon to an output file """
    os.system('echo ------------------------------------------------ >> "C:\\BugBounty\\test2.txt"')
    os.system('nmap.exe -sT -p- -oN c:\\BugBounty\\test2.txt ' + ip)
    os.system('echo ------------------------------------------------ >> "C:\\BugBounty\\test2.txt"')
    os.system(r'C:\nikto\nikto.bat -output C:\\BugBounty\\test2.txt -host ' + ip)
    
    
automation("216.18.168.66")