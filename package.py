#!/usr/bin/env python
#-*-coding:utf-8-*-
'   a test moudle     '
__author__="John Wen"
import sys

def test():
    args=sys.argv
    if len(args)==1:
        print("Hello World!!")
    elif len(args)==2:
        print("Hello , %s!"% args[1])
    else:
        print("too many args")

if __name__=='__main__':
    test()
