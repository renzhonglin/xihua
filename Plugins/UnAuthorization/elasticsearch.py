import requests
from urllib.parse import urlparse
requests.packages.urllib3.disable_warnings()

name = 'ElasticSearch 未授权访问漏洞'


def run(url):
    headers = {
    'Content-Type':'text/xml',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    host = urlparse(url)
    url = f"{host.scheme}://{host.netloc}"
    try:
        vulurl = url + '/_cat'
        response = requests.get(vulurl, headers=headers, timeout=15, verify=False)
        if '/_cat/allocation' in response.text:
            return ['True',name,vulurl]
        else:
            try:
                vulurl = url + '/_nodes'
                response = requests.get(vulurl, headers=headers, timeout=15, verify=False)
                if 'elasticsearch' in response.text:
                    return ['True',name,vulurl]
                else:
                    return ['False',name]
            except Exception as e:
                return ['False',name]
    except Exception as e:
        return ['False',name]

if __name__ == '__main__':
    url = 'http://192.168.123.46:8080/'
    print(run(url))