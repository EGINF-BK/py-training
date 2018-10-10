# -*- coding=utf-8 -*-

url = r'D:\Users\010500571\Desktop\py-training\homework\access.log.txt'

def open_file(url):
    total_list = []
    f = open(url,'r')
    data = f.readlines()
    f.close()
    for line in data:
        line = line.strip('\n')
        total_list.append(line.split(' '))
    #for i in range(len(total_list[0])):
    #    print total_list[0][i],i
    return total_list

#open_file(url)

def calculate_pv_uv():
    data = open_file(url)
    pv = []
    uv = []
    for item in data:
        pv.append(item[0])
    pv_count = len(pv)
    print pv_count
    uv = set(pv)
    uv_count = len(uv)
    print uv_count

def top_resource(url,num):
    data = open_file(url)
    url_dict = {}
    dict_sorted = {}
    url_list = []
    for item in data:
        item = item[10].strip('"')
        if item != '-':
            url_list.append(item)
    for item in set(url_list):
        url_dict.setdefault(item, 1)
    for item in url_list:
        if url_dict.get(item):
            url_dict[item] += 1

    dict_sorted = sorted(url_dict.items(),key=lambda e:e[1],reverse = True)

    for i in range(num):
        print dict_sorted[i][0],':',dict_sorted[i][1]

top_resource(url,5)

def web_availabe_rate(url):
    data = open_file(url)
    url_list = []
    availabe_count = 0
    unavailabe_count = 0
    for item in data:
        url_list.append(int(item[8]))
    for item in url_list:
        if item == 200:
            availabe_count += 1
        else:
            unavailabe_count += 1
    #print availabe_count,unavailabe_count
    total_count = len(url_list)
    availabe_rate = float(availabe_count)/total_count
    unavailabe_rate = float(unavailabe_count)/total_count
    print repr(round(availabe_rate*100,2))+'%',repr(round(unavailabe_rate*100,2))+'%'
    return availabe_rate,unavailabe_rate

#web_availabe_rate(url)

