import os
import re
import socket
import struct

ans = os.popen('ifconfig')

def hash_ip():
    rst = {}
    list_ip = []
    list_card = []
    card_tmp = []
    hash_list = []
    l = []

    for each in ans:
        l.append(str(each))

    for index, each in enumerate(l):
        cards = re.findall(r"^\w+",each)
        
        if cards != []:
            card_tmp.append(str(cards[0]))
        word_ip = re.findall(r"^inet\s[^\r\n]+?\s$",each.lstrip())

        if word_ip != []:
            word_ip = str(word_ip)
            
            word_card = l[int(index) - 1].split(':')[0]
            list_card.append(word_card)
            
            word_ip_new = word_ip.split(' ') 
            inet_each = word_ip_new[1]
            list_ip.append(inet_each)
    
    
    for i in list_card:
        if i in card_tmp:
            card_tmp.remove(i)
    
    for i in card_tmp:
        list_card.append(i)
    
    if list_card > list_ip:
        count = len(list_card) - len(list_ip)
        
        while(count != 0):
            list_ip.append('null')
            count -= 1
    print(list_ip)
    print(list_card) 
    
    for ip in list_ip:
        
        if ip != 'null':
            ip = socket.ntohl(struct.unpack("I", socket.inet_aton(str(ip)))[0])
            hash_list.append(ip)
    
    tmp = []

    for i in hash_list:
        t = i % 7
        tmp.append(t)
    
    rst = dict(map(lambda x,y:[x,y],tmp,list_card))

    print(rst)
    
    return rst

    ans.close()
hash_ip()
