import pymongo
from urllib.parse import urlparse

name = 'Mongodb 未授权访问漏洞'


def run(url):
    try:
        vulurl = urlparse(url)
        host = vulurl.netloc.split(':')
        ip,port = host[0],int(host[1])
        conn = pymongo.MongoClient(ip,port)
        db = conn.database_names()
        conn.close()
        return ['True',name,f'{ip}:{port}']
    except Exception as e:
        return ['False',name]


if __name__ == '__main__':
    url = 'http://127.0.0.1:27017/'
    print(run(url))