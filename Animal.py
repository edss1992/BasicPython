#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
私有是类私有，而不是参数私有。而且python不用申明变量类型。
'''
class Animal(object):
    def __init__(self,name,sound):
        self.__name=name
        self.__sound=sound
    def run(self):
        print("Animal is rnning")

class dog(Animal):
    def run(self):
        print("Dog is running")
    def sound(self):
        print("Dog is wangwang")
class cat(Animal):
    pass

def twice(animal):
    animal.run()
    animal.sound()#没办法指定类型。所以这里的参数只是普通的参数
                  #没办法实现父类变量指向子类对象。因为根本就没有指定变量类型
                  #所以只要有这个run或者sound方法就可以直接运行

'''
这里的继承跟java的不一样。这是动态语言的鸭子类型
只要这个类有这个方法就可以被认为是同一个类
'''
d=dog('dog','wangwang')
#d.run()
a=Animal('Animal',None)
twice(d)
twice(a)

