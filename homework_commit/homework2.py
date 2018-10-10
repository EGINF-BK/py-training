# -*- coding=utf-8 -*-
import os
from os import path

file_path = r'c:\windows\system32'

#file_name = os.listdir(file_path)
#for name in file_name:
    #print name

def getdirsize(file_path):
    size = 0
    for root,dirs,files in os.walk(file_path):
        size += sum(path.getsize(path.join(root,name)) for name in files)
    return size
#print getdirsize(file_path)

def listdir(file_path):
    for root,dirs,files in os.walk(file_path):
        size = getdirsize(root)
        if round(float(size)/(1024*1024),2)>200:
            print root,str(round(float(size)/(1024*1024),2))+'MB'
listdir(file_path)

