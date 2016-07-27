#!/usr/bin/env python
#-*-coding:utf-8 -*-
'''
author:johnw
date:2016/07/27

'''
L=[
    ['Apple','Google','Microsoft'],
    ['Java','python','ruby','php'],
    ['Adam','bart','Lisa']
  ]

print(L[0][0])     # Apple
print(L[1][1])     # python
print(L[2][2])     # lisa

classmates=['Michael','Bob','Tracy']
print('classmates = ',classmates)
print('classmates[0] = ',classmates[0])
print('classmates[-1] = ',classmates[-1])#Tracy
classmates.pop()
print('classmates = ',classmates)
print('len(classmates) = ',len(classmates))
#insert
#pop

classmate=('Michael','Bob')
#TypeError: 'tuple' object does not support item assignment
#classmate[0]='Adma'

