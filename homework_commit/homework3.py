# -*- coding: utf-8 -*-
from homework1 import load_file_path
from collections import  Counter
from os import path

file_name = 'Princess White Flame.txt'
dir_name = 'homework'


def find_location(file_path,para):
    with open(file_path) as f:
        pre_num = f.tell()
        data = f.readline()
        while data:
            pre_num = f.tell()
            if data.strip('\n').strip(' ') in para:
                 print 'start:',pre_num,data
                 data = f.readline()
                 print 'end:',f.tell()
            else:
                data = f.readline()





def open_file(file_path):#以列表形式返回，列表中的每个元素分别为txt中的一个段落。
    book_list = []#整本书作为一个列表，段落作为列表的基本元素
    para_list = []#段落列表，列表中的元素为段落中的每行
    try:
        with open(file_path,'r') as f:
            total_list = f.readlines()
    except:
        print file_name + 'Not found'
    i = 0
    while i <= len(total_list)-1:#提取书中的段落，并加到book_list作为一个列表元素
        if total_list[i].strip():
            para_list.append(total_list[i].strip('\n'))
            i += 1
        elif total_list[i-1].strip() and not total_list[i].strip():
            book_list.append(' '.join(para_list))
            para_list = []
            i += 1
        else:
            i += 1
    return book_list


def count_word(paragraph_list,num):
    word_num = Counter()
    para_most = {}#段落字典，key为paragraph_list列表中的索引，value为此索引对应的段落的词的个数
    for i,paragraph in enumerate(paragraph_list):
        word_list = [(word.strip('.').strip('“').strip('”').strip(',')).lower() for word in paragraph.split(' ')]#将列表中的每个元素，即每个段落按词切成一个列表。
        para_most[repr(i)] = len(word_list) #将此段落词的个数赋给paragraph_list列表索引
        for item in filter(None,word_list):
            word_num[item] += 1
    print "本文总词数为:",sum(word_num.values())
    sort_dict = sorted(para_most.items(),key=lambda e:e[1],reverse=True)#将para_most按value值降序排序
    print "出现单词最多的前%d个："%num,word_num.most_common(num)
    return paragraph_list[int(sort_dict[0][0])]

def main():
    file_path = load_file_path(dir_name,file_name)
    paragraph_list = open_file(file_path)
    para = count_word(paragraph_list,5)
    print para
    find_location(file_path,para)
    with open(path.join(path.dirname(file_path),'most largest paragraph.txt'),'w') as f:
        f.write(para)#将最大段落写入同级目录下的most largest paragraph.txt文件中


if __name__ == '__main__':
    main()



