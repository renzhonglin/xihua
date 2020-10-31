import memcache
from urllib.parse import urlparse

name = 'Memcached 未授权访问漏洞'


def run(url):
    try:
        vulurl = urlparse(url)
        host = vulurl.netloc.split(':')
        ip,port = host[0],int(host[1])
        mc = memcache.Client([f'{ip}:{port}'], debug=True)
        if 'version' in str(mc.get_stats()):
            return ['True',name,f'{ip}:{port}']
        else:
            return ['False',name]
    except Exception as e:
        return ['False',name]


if __name__ == '__main__':
    url = 'http://107.182.179.149:11212/'
    print(run(url))


