import redis
from urllib.parse import urlparse

name = 'Redis 未授权访问漏洞'


def run(url):
    try:
        vulurl = urlparse(url)
        host = vulurl.netloc.split(':')
        ip,port = host[0],int(host[1])
        content = redis.Redis(ip,port,db=0)
        db = content.info()
        return ['True',name,f'{ip}:{port}']
    except Exception as e:
        return ['False',name]

if __name__ == '__main__':
    url = 'http://192.100.101.33:7479/'
    print(run(url))