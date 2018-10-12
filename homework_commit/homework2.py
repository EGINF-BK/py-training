# -*- coding=utf-8 -*-
import os
from os import path

file_path = path.join('c:',path.sep,'windows','system32')

def getdirsize(file_path):
    size = 0
    for root,dirs,files in os.walk(file_path):
        size += sum(path.getsize(path.join(root,name)) for name in files)
    return size


def listdir(file_path,size):
    for root,dirs,files in os.walk(file_path):
        for file in files:
            size_file = getdirsize(path.join(root, file))
            if round(float(size_file) / (1024 * 1024), 2) > size:
                print path.join(root, file), str(round(float(size_dir) / (1024 * 1024), 2)) + 'MB'
        size_dir = getdirsize(root)
        if round(float(size_dir)/(1024*1024),2) > size:
            print root,str(round(float(size_dir)/(1024*1024),2))+'MB'

listdir(file_path,200)

