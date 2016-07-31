#!/usr/bin/env python
#-*-codingutf-8-*-
'''
1.函数有一个参数：__name__
2.装饰器在代码运行期间动态增加功能
3.
4.
'''
import functools
import time
def log(func):
    def wrapper(*args,**kw):
        print("Call %s ():"%func.__name__)
        return func(*args,**kw)
    return wrapper


def logText(text):
    def decoration(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s:%s'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decoration

def logTime(text):
    def decoration(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            start=time.clock()
            print("Begin call %s() and \'%s\' (textcontent)"%(func.__name__,start))
            r=func(*args,**kw)
            end=time.clock()
            print("end call %s() and \'%s\' (textcontent)"%(func.__name__,end))
            print('This Program waste %s of time'%(end-start,))
            return r
        return wrapper
    return decoration

'''
callable 判断一个参数是否可以调用。如果是函数，可以调用就返回True。
如果不可以调用就返回False
'''
def checkLog(*text):
    if callable(text):
        print(callable(text))
        def wrapper(*args,**kw):
            print('.....call %s()'%text.__name__)
            return text(*args,**kw)
        return wrapper
    else:
        print(callable(text))
        def decoration(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print('call %s +++ %s'%(func.__name__,text))
                return func(*args,**kw)
            return wrapper
        return decoration



   
@checkLog()
def now():
    print('2016-07-30')
now()

