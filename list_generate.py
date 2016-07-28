#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
缺点：直接生成。容量有限。
'''
L=['Hello','world',19,'Apple',20,None]
print([x.lower() for x in L if isinstance(x,str) ])
