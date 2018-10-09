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

#example1  no paramaters in func
#******************************************************
def show_time(f):
   """docstring for show_time"""
   def wrapper():
       start = time.time()
       f()
       end = time.time()
       print('This function {} cost {:.3f} seconds'.format(f.__name__,float(end-start)))
   return wrapper

@show_time
def foo():
   """docstring for foo"""
   print('this is foo function...')
   time.sleep(1)

foo()     
# #******************************************************


#for the small or middle data, we can use open all the elements of list in memory
#egg_list and egg_list1 are the same result
@show_time
def foo1():
    print('{:*^20}'.format('1st sample'))
    egg_list = []
    for i in range(999999):
        egg_list.append('egg{}'.format(i))
    time.sleep(1)

@show_time
def foo2():
    print('{:*^20}'.format('2ed sample'))
    egg_list1 = [ 'egg{}'.format(i) for i in range(999999) ]
    print (len(egg_list1))
    time.sleep(1)

#for the big/huge data, we can't open all the elements of list in memory
#we should use generator_list, this method will only get one element and
#transfer to memory, it's low capcity cost. 
@show_time
def foo3():    
    print('{:*^20}'.format('3rd sample'))
    egg_list2 = ( 'egg{}'.format(i) for i in range(999999) )
    print(egg_list2.__sizeof__)
    time.sleep(1)

foo1()
foo2()
foo3()



