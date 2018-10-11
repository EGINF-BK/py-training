#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import string

s=open(r"D:\Users\081205132\Desktop\py-training\homework\access.log.txt","rb").read()
results=re.findall("(?isu)(http\://[a-zA-Z0-9\.\?/&\=\:]+)",s)
open("urls.txt", "w").write("".join(results) + "\r\n")
from collections import  Counter
print Counter(str(i) for i in results)
print 'finished'