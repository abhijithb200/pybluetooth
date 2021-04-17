
from bluetooth import *
from PyOBEX.client import Client 
import sys

addr = sys.argv[1]
file = sys.argv[2]
print("Searching for OBEX service on %s" % addr)

service_matches = find_service(uuid="00001105",address = addr )
if len(service_matches) == 0:
    print("Couldn't find the service.")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"%s\" on %s" % (name, host))
client = Client(host, port)
client.connect()
client.put(file,bytes("hii",'UTF-8'))
client.disconnect()
