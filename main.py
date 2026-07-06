import socket
import sys
from datetime import datetime as dt


# python main.py Domain(www.google.com)
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid syntax!!!")
    print("Syntax will be: python port.py <ip/domain>")
    sys.exit()

# add banners for styling
print("-" * 50)
print(f"Target IP: {target}")
# time start scanning
time1 = dt.now()
print(f"Start Time: {str(time1)}")
print("-" * 50)

# check port is open or close
checkPort = False

try:
    for port in range(80, 100):
        search = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.3)

        print(f"Scanning the ports: {port}")
        result = search.connect_ex((target, port))

        if result == 0:
            checkPort = True
            print(f"The open port is: {port}")
        search.close()

except KeyboardInterrupt:
    print("\nKey has been pressed!") # press ctrl/c
    sys.exit()
except socket.gaierror:
    print("\nThe host is close!!") # spelling error
    sys.exit()
except socket.error:
    print("\nCould not find server!!!") # no internet connection
    sys.exit()

# time ending
time2 = dt.now()
if(checkPort == False):
    print("None of the port is open")
print(f"The time latency or time taking: {time2 - time1}")
print("-" * 50)
