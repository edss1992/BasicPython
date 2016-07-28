#!/usr/bin/env python
#-*-coding:utf-8-*-
d={'Michael':95,'bob':78,'tracy':98}
print(d['Michael'])
d['jack']=100
print(d.get('jack'))
print(d.get('john','Not exist'))
d.pop('bob')
print(d)
s=set(['Michael',1,2,3,True])

