#!/usr/bin/env python
#-*-coding:utf-8-*-
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def get_score(self):
        print("%s:%s"%(self.__name,self.__score))
bart=Student('bart',100)
bart.get_score()
