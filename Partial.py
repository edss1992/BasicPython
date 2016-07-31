#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
functools.partial的作用就是，
把一个函数的某些参数给固定住（也就是设置默认值），
返回一个新的函数，调用这个新函数会更简单。

'''
print(int('123',base=8))
print(int('123',16))

import functools
int8=functools.partial(int,base=8)
print(int8('123'))

'''
小结：
当函数的参数个数太多，需要简化时，
使用functools.partial可以创建一个新的函数，
这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
'''
