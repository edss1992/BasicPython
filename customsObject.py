#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
定制类

__slots__
__len__
__str__
__repr__
__iter__  for循环
__getitem__ 得到下标 d[0]

'''
class Fib(object):
    
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        #slice是什么意思？？
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L
        
    def __item__(self):
        return self
    def __getattr__(self,attr):
        if attr='test':
            return "Testing"
    def __call__(self):
        pass

