#!/usr/bin/env python
#-*- coding: utf-8 -*-
#*************************************************************************
#    > File Name: generator_list_test.py
#    > Author: Tim Wang
#    > Mail: spookw@foxmail.com
#    > Created Time: Tue 22 May 2018 11:20:57 PM CST
# ************************************************************************/

from __future__ import print_function
import time 

#example2   parameters in func
#******************************************************
def show_time(f):
   """docstring for show_time"""
   def wrapper(*xj):
       start = time.time()
       f(*xj)
       end = time.time()
       print('This function {} cost {:.3f} seconds'.format(f.__name__,float(end-start)))
   return wrapper

@show_time
def add(*nums):
   """docstring for foo"""
   sums = 0
   for i in nums:
       sums += i
   time.sleep(1)
   print('the sum is {}'.format(sums))

add(1,3,4,1,1)
# ******************************************************



