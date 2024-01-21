import requests

def main():
    api_path = "http://10.32.1.188:8080/api"
    basic_auth = ("admin", "admin")
    accept_list = [
        "application/vnd.yang.api+json",
        "application/vnd.yang.datastore+json",
        "application/vnd.yang.data+json",
        "application/vnd.yang.collection+json",
    ]
    get_headers = {"Accept": ",".join(accept_list)}

    post_headers = {"Content-Type": "application/vnd.yang.data+json"}
    get_resp = requests.get(
        f"{api_path}/running/devices/device",
        auth=basic_auth,
        headers=get_headers
    )

    devices = get_resp.json()["collection"]["tailf-ncs:device"]

    print(devices)


if __name__ == "__main__":
    main()