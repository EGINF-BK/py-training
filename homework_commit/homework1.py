# -*- coding=utf-8 -*-
from os import path

file_name = 'access.log.txt'
current_name = 'homework1'

def load_file_path(file_name):
    current_path = path.abspath(current_name)
    father_path = path.abspath(path.dirname(current_path)+path.sep+'..')
    file_path = 'homework\\'+file_name
    return path.join(father_path,file_path)


file_path = load_file_path(file_name)


def open_file(file_path):
    total_list = []
    f = open(file_path,'r')
    data = f.readlines()
    f.close()
    for line in data:
        line = line.strip('\n')
        total_list.append(line.split(' '))
    return total_list


data = open_file(file_path)


def calculate_pv_uv(file_path):
    data = open_file(file_path)
    pv = [item[0] for item in data]
    print 'PV:',len(pv)
    print 'UV:',len(set(pv))


def top_resource(file_path,num):
    data = open_file(file_path)
    resource_dict = {}
    resource_total = []
    for i in range(len(data)):
        resource_single = [x for x in data[i][6].split('/') if x != '']
        if resource_single:
            resource_total.append(resource_single[0])
    for item in set(resource_total):
        resource_dict.setdefault(item, 1)
    for item in resource_total:
        if resource_dict.get(item):
            resource_dict[item] += 1
    dict_sorted = sorted(resource_dict.items(),key=lambda e:e[1],reverse = True)
    for i in range(num):
        print dict_sorted[i][0],':',dict_sorted[i][1]


def web_availabe_rate(file_path):
    data = open_file(file_path)
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
    total_count = len(url_list)
    availabe_rate = float(availabe_count)/total_count
    unavailabe_rate = float(unavailabe_count)/total_count
    print repr(round(availabe_rate*100,2))+'%',repr(round(unavailabe_rate*100,2))+'%'
    return availabe_rate,unavailabe_rate


def main(file_path):
    calculate_pv_uv(file_path)
    top_resource(file_path, 5)
    web_availabe_rate(file_path)

main(file_path)