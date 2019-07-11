import time
import requests
import datetime
import json
import sys

# CALLS CURL
# EVERYTHINGS IS IN link: https://github.com/Netflix/ndbench/wiki/REST

CONNECT_CLIENT="http://localhost:8080/REST/ndbench/driver/init/CassJavaDriverGeneric"
DISCONNECT_CLIENT="http://localhost:8080/REST/ndbench/driver/shutdownclient"
GET_INFO="http://localhost:8080/REST/ndbench/driver/getserverstatus"
START_WRITES="http://localhost:8080/REST/ndbench/driver/startWrites"
STOP_WRITES="http://localhost:8080/REST/ndbench/driver/stopWrites"
START_READS="htpp://localhost:8080/REST/ndbench/driver/startReads"
STOP_READS="http://localhost:8080/REST/ndbench/driver/stopReads"
START_AMBOS="http://localhost:8080/REST/ndbench/driver/start"
STOP_AMBOS="http://localhost:8080/REST/ndbench/driver/stop"

f = open("file_result.txt", "w")

ti20=time.time()
ta20=0

print("Connecting Plugin CassJavaDriverGeneric...")
r = requests.get(CONNECT_CLIENT)
print(r.status_code)
if(r.status_code != 200):
    sys.exit()
print("Success!!!")

# IF ONLY WRITE (remove ''')
'''
print("Starting Writes...")
r = requests.get(START_WRITES)
print(r.status_code)
if(r.status_code != 200):
    sys.exit()
print("Writes initiated a success!!!")
'''

# IF ONLY READ (remove ''')
'''
print("Starting Reads...")
r = requests.get(START_READS)
print(r.status_code)
if(r.status_code != 200):
   sys.exit()
print("Reads initiated a success!!!")
'''

# IF FOR BOTH (remove ''')
'''
print("Starting Writes/Reads...")
r = requests.get(START_AMBOS)
print(r.status_code)
if(r.status_code != 200):
   sys.exit()
print("Writes/Reads initiated a success!!! ")
'''

while(ta20 < (25*60)):
    ti5=time.time()
    ta5=0
    print("get info")
    r = requests.get(GET_INFO)
    print(r.status_code)
    data = r.json()
    data["currentTime"] = str(datetime.datetime.now())
    data_as_text = json.dumps(data, indent=2)
    f.write(data_as_text)
    while(ta5 < 1):
        #print("dentro 5s")
        tf5=time.time()
        ta5=tf5-ti5
        #print(ta5)
    print("Fim 5s")
    tf20=time.time()
    ta20=tf20-ti20

# FINALIZE ALL OPERATIONS
print("Finishing ALL...")
r = requests.get(STOP_AMBOS)
print(r.status_code)
if(r.status_code != 200):
    sys.exit()
print("Finalized ALL!!!")


f.close()

# DISCONNECTS CLIENT
print("Disconnecting Client...")
r = requests.get(DISCONNECT_CLIENT)
print(r.status_code)
if(r.status_code != 200):
    sys.exit()
print("Cliente Desconnected!!!")
