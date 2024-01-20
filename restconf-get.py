import requests
import json
from pprint import pprint
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

router = {"ip": "10.32.1.210", "port":"443", "user":"cisco","password":"cisco"}

headers = {"Accept": "application/yang-data+json", "Content-Type":"application/yang-data+json"}

url = f"https://{router['ip']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

response = requests.get(url, headers=headers, auth=(router['user'], router['password']), verify=False)

api_data = response.json()

print("/" * 50)
pprint(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
print("/" * 50)
if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == 'if-state-up':
    print('Interface is up')

