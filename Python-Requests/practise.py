import requests
import json
url = "https://172.27.6.141:8834/session"
username = "rsysuser"
password = "MediaE%6"


def get_token(url,username,password):
    data = {"username":username,
            "password":password
            }
    response = requests.request("POST", url=url, data=data,verify=False)
    print(response.status_code)

    op = json.loads(response.text)
    print(op["token"])
    return op["token"]

def get_scan(token):
    print(token)
    header = {
            'X-Cookie':'token='+str(token),
            "Content - Type": "application / json"
        }
    url = "https://172.27.6.141:8834/scans"
    response = requests.request(method='GET',url=url, headers=header, verify=False)
    print(response.text)


token = get_token(url,username,password)
get_scan(token)
