#!/bin/bash
echo "输入标题(text)"
read name
echo "输入内容"
read gmail
echo "输入发件人"
read title

# 判断是否有输入参数
if [ $# -eq 0 ];then

#    basename:只输出路劲的最后一个名称
    echo -e "\033[34mUsage: `basename $0` filename.txt\033[0m"    
fi

# 判断是否输入的是文件
if [ ! -f $1 ];then
    echo -e "\033[33mError file(It's not a file)\033[0m"
    exit    
fi

# 从文件读取ip地址
for ip in `cat $1`
do
    swaks --body "$gmail" --header "Subject:$name" -t $ip -f "$title" >/dev/null 4>&1
    if [ $? -eq 0 ];then
        echo -e "\033[33m${ip} is up\033[0m"
    else
        echo -e "\033[33m${ip} is down\033[0m"
    fi
done
