import subprocess as splt
import os
import time as t

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
    start_time = t.perf_counter()  # Start the timer
    pingcommand = ping_result(host, flag)
    end_time = t.perf_counter()  # End the timer
    scan_results[host] = (pingcommand.returncode == 0, end_time - start_time)  # Store both result and time

# Check the return code to determine if the ping was successful
for host, finishedresult in scan_results.items():
    if finishedresult[0]:
        print(f"{host}: Up (Time: {finishedresult[1]:.2f} seconds)")
    else:
        print(f"{host}: Down (Time: {finishedresult[1]:.2f} seconds)")

input("Press Enter to exit...")

# Praise Jesus!

