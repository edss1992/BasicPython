#!/usr/bin/env python
#-*-coding:utf-8-*-
from collections import Iterable,Iterator
def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1,2,3]:',isinstance([1,2,3],Iterable))
print('Iterable? \'abc\':',isinstance('abc',Iterable))
print('Iterable? 123:', isinstance(123,Iterable))
print('Iterable?g()',isinstance(g(),Iterable))
print('*******************************')
print('Iterable? [1,2,3]:',isinstance([1,2,3],Iterator))
print('Iterable? \'abc\':',isinstance('abc',Iterator))
print('Iterable? 123:', isinstance(123,Iterator))
print('Iterable?g()',isinstance(g(),Iterator))

print("**********************************")
it=iter([1,2,3,4,5])
print(next(it))
d={'a':1,'b':2,'c':3}
print('****************keys********************')
for k in d.keys():
    print(k)
print('****************values********************')
for v in d.values():
    print(v)
print('******************items******************')
for k,v in d.items():
    print(k,v)
print('**************enumerate**********************')
for i,v in enumerate(['A','B','C']):
    print(i,v)

