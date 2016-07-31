#!/usr/bin/env python
#-*-coding:utf-8-*-
print(type(123))
print(isinstance(123,object))
#获得一个对象的所有属性和方法可以用 dir()
print(dir(str))
#在程序运行时给class加上功能？
#就是使用__slots__限定好要添加的属性。在创建实例的时候
#进行设置
#对于这种设置，子类是不起作用的
class student(object):
    __slots__=('name','score')

s=student()
s.name='aaa'

#如何在python里面使用getter和setter方法？
#使用getter-----》@property
#使用setter----》@score.setter
#一般属性是不暴露的，这样设置以后。就可以使用例如
#s.score=xxxx
#s.score
#在设置的方法里面还有判断的执行语句
class student2(object):
    @property
    def birth(self):
        return self.__birth
    @birth.setter
    def birth(self,v):
        self.__birth=v

s=student2()
s.birth=1992
print(s.birth)
'''
学习了__slots__ 动态的给运行中的类绑定属性
@property 设置getter和setter方法更加简便

'''


