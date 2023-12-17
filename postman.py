import requests

url = "https://10.32.1.210/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"

payload = {}
headers = {
  'Authorization': 'Basic Y2lzY286Y2lzY28='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)