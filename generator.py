#!/usr/bin/env python
#-*-coding:utf-8-*-
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n+=1
    return 'Done'

f=fib(6)
for i in f:
    print(i)
