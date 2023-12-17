import requests
import json

url = "http://10.32.1.205/ins"

payload = json.dumps({
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show ip int brief",
    "output_format": "json"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic Y2lzY286Y2lzY28='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
