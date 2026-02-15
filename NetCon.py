import subprocess as splt
import os

# Lists and dictionaries to store hosts and results
hosts = []
scan_results = {}

# Function to ping a host and return the result
def ping_result(host, countcommand):
    return splt.run(['ping', host, countcommand,'3'], capture_output=True, text=True)

print("Enter IP addresses or hostnames (Press Enter on a blank line to finish):")

# Loop to get multiple hosts until the user enters a blank line
while True:
        host = input("> ").strip()
        if host == "":   # Stop if blank
            break   
        hosts.append(host)

if os.name == 'nt':  # Windows
    flag = '-n'  # Use '-n' for Windows    
else:  # Unix/Linux/Mac
    flag = '-c'  # Use '-c' for Unix/Linux/Mac

# Ping each host and store the results
for host in hosts:
    pingcommand = ping_result(host, flag)
    scan_results[host] = pingcommand.returncode == 0 # Store True for success, False for failure

# Check the return code to determine if the ping was successful
for host, finishedresult in scan_results.items():
    if finishedresult:
        print(f"{host}: Up")
    else:
        print(f"{host}: Down")

input("Press Enter to exit...")

