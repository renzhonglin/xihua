import os
import importlib.machinery
r = input("输入检测链接:(http://172.23.161.231:14210/):")

def main(poc, url):
    check = importlib.machinery.SourceFileLoader(poc, poc).load_module()
    return check.run(url)


Plugins = "Plugins"
for application in os.listdir(Plugins):
    file_path = os.path.join(Plugins, application)
    for path, dirs, file_poc in os.walk(file_path):
        for lists in file_poc:
            poc = f'{Plugins}/{application}/{lists}'
            if poc.endswith('.py'):
                result = main(poc, r) ##lianjie
                print(result)