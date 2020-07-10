import sys
import requests

# If the argument is less than 2 or more 3, then raise error and finish
# the program
if len(sys.argv) not in [2, 3]:
    print("You are missing the arguments!")
    print("Please input the server's address, it can be ip address or the domain name (requiered) ")
    print("Please input the server's port (value between 1 65535 and ) (optional)")
    exit(1)

ipAddr = sys.argv[1]

try:
    if len(sys.argv) == 3:
        port = sys.argv[2]
        # be sure that the port number is between 1 and 65535
        assert ((int(port) >= 1) and (int(port) <= 65535))
    else:
        port = "80"
except AssertionError:
    print("The port number is not valid!!")
    exit(2)

url = "http://" + ipAddr + ":" + port + "/"

h_header = {"Connection": "Close"}
try:
    reply = requests.head(url, headers=h_header)
except requests.exceptions.InvalidURL:
    print("The URL is not valid:", url)
    exit(3)
except requests.exceptions.ConnectionError:
    print("Can't connect to the address:", ipAddr)
    exit(4)
except requests.RequestException:
    print("Error getting data from the server!!")
    exit(5)
else:
    print(reply.status_code, reply.reason)
