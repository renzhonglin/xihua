import requests
from urllib.parse import urlparse
requests.packages.urllib3.disable_warnings()

name = 'CouchDB 未授权访问漏洞'


def run(url):
    headers = {
    'Content-Type':'text/xml',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    host = urlparse(url)
    url = f"{host.scheme}://{host.netloc}"
    try:
        vulurl = url + '/_utils/'
        response = requests.get(vulurl, headers=headers, timeout=15, verify=False)
        if 'Project Fauxton' in response.text and '<strong>requires</strong>' in response.text:
            return ['True',name,vulurl]
        else:
            return ['False',name]
    except Exception as e:
        return ['False',name]

if __name__ == '__main__':
    url = 'http://107.182.179.149:5984/'
    print(run(url))