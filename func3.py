#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
函数的参数
    1.默认参数，但是我们还是可以继续传值替换默认参数。默认参数必须指定不变对象，否则就会进行累加
    2.可变参数，用 *number 代表可变参数 在函数里面直接使用number。传入时，随意传入参数。如果是一个list。则需要传入 *listName
    3.关键字参数，用 **kw 代表关键字参数。在函数里面直接使用kw。 传入时，city='beijing'.如果是一个dict。则传入 **dictName
    4.命名关键字。如果要限制传入的参数。ex：def example(name,age,*,city,job) 就必须传入city job.调用方法如下
'''
def person(name,age,*args,city,job):
    print(name,age,city,job)

person('john',11,1,11,city='beijing',job='CEO')

print("********************************************")
def Hello(greeting,*args):
    if(len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s,%s!' % (greeting,','.join(args)))

Hello('Hi')
Hello('Hi','sala')
Hello('Hi','Michael','Bob')
name=('jimmy','jacob')
Hello('Hello',*name)

print("************************************************")
def print_scores(**kw):
    print("name    scores")
    print('--------------')
    for name,score in kw.items():
        print('%3s   %d' % (name,score))

print_scores(Amam=99,john=100,bab=90)

data={
    'john':1000,
    'jimy':900,
    'jacob':809
}

print_scores(**data)

print("***********************************************")

def print_info(name,age,*,city="fujian",gender):
    print("name : %s"  % name )
    print("age : %s " % age )
    print('city : %s ' % city )
    print('gender : %s ' % gender )
    print()

print_info('johnw',11,gender="man")
