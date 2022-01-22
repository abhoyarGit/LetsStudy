import requests
import json
url = "https://172.27.6.141:8834/session"
username = "rsysuser"
password = "MediaE%6"

def get_token(url,username, password):
    data = {'username' : username,
            'password' : password }
    responce = requests.request('POST',url=url,data=data, verify=False)
    #print(responce.text)
    op = json.loads(responce.text)
    return op['token']


def get_scan(url,username, password):
    data = {'username': username,
            'password': password}
    token = get_token(url,username,password)
    print(token)
    if token:
        header = {
            'X-Cookie':'token='+token,
            "Content - Type": "application / json"
        }
        url = "https://172.27.6.141:8834/scans"
        #responseScan = requests.get(url=url,headers=header, verify=False)
        responseScan = requests.request(method='GET',url=url,headers=header, verify=False)
        print(responseScan.text)

def get_policies(url,username,password):
    token = get_token(url,username,password)
    if token:
        url = "https://172.27.6.141:8834/policies"
        header = {'Content-Type': 'application/json',
                  'X-Cookie': 'token='+token}
        resPolicy = requests.request(method='GET',url=url , headers=header, verify=False)
        print(resPolicy.text)

get_scan(url,username,password)
#get_policies(url,username,password)
