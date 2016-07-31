#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
def dir_l(path):
    l=os.listdir(os.path.abspath(path))
    for file in l:
        print(file)

#dir_l('D:\\')
path=input("Please enter where u want to search for:")

index=input("what type of file you want to find : ")

def searchAndListFile(path,index):
    for x in os.listdir(os.path.abspath(path)):
        x=os.path.join(path,x)
        if os.path.isfile(x) and os.path.splitext(x)[1]==index:
            print(x)
        elif os.path.isdir(x):
            searchAndListFile(x,index)
        
searchAndListFile(path,index)

'''
os:
    listdir
    mkdir
    rmdir
    environ
    name
    uname()
    os.rename()
    os.remove()
os.path:
    abspath
    isfile
    isdir
    join
    splitext
'''
