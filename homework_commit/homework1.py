# -*- coding=utf-8 -*-
from os import path

file_name = 'access.log.txt'
dir_name = 'homework'

def load_file_path(dir_name,file_name):
    father_dir_path = path.abspath(path.dirname(__file__)+path.sep+'..')
    return  path.join(father_dir_path,dir_name,file_name)


def open_file(file_path,n):
    total_list = []
    try:
        with open(file_path ,'r') as f:
            for line in f.readlines():
                total_list.append(line.strip('\n').split()[n])
    except:
        print file_name+'Not Found'
    return total_list


def calculate_pv_uv(file_path):
    data = open_file(file_path,0)
    pv = [item for item in data]
    print 'PV:',len(pv)
    print 'UV:',len(set(pv))


def top_resource(file_path,num):
    data = open_file(file_path,6)
    resource_dict = {}
    resource_total = []
    for i in range(len(data)):
        resource_single = filter(None, data[i].split('/'))
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
    data = open_file(file_path,8)
    url_list = []
    availabe_count = 0
    unavailabe_count = 0
    for item in data:
        url_list.append(int(item))
    for item in url_list:
        if item >= 400:
            unavailabe_count += 1
        else:
            availabe_count += 1
    total_count = len(url_list)
    availabe_rate = float(availabe_count)/total_count
    unavailabe_rate = float(unavailabe_count)/total_count
    print repr(round(availabe_rate*100,2))+'%',repr(round(unavailabe_rate*100,2))+'%'
    return availabe_rate,unavailabe_rate


def main():
    file_path = load_file_path(dir_name,file_name)
    calculate_pv_uv(file_path)
    top_resource(file_path, 5)
    web_availabe_rate(file_path)

if __name__ == '__main__':
    main()