import requests
from urllib.parse import urlparse
requests.packages.urllib3.disable_warnings()

name = 'Apache Hadoop YARN 资源管理器 REST API 未授权访问漏洞'


def run(url):
    headers = {
        'Content-Type': 'text/xml',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    host = urlparse(url)
    vulurl = f"{host.scheme}://{host.netloc}/ws/v1/cluster/info"
    try:
        response = requests.get(vulurl, headers=headers, timeout=15, verify=False)
        if 'resourceManagerVersion' in response.text:
            return ['True', name, vulurl]
        else:
            return ['False', name]
    except Exception as e:
        return ['False', name]


if __name__ == '__main__':
    url = 'http://172.26.102.29:8088/'
    print(run(url))
