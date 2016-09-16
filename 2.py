import os
import re
ans = os.popen('ifconfig')
def get_ip():
    list_ip = []
    list_card = []
    card_tmp = []
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
    
    
    
    return list_ip


    ans.close()
get_ip()
