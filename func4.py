#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
汉诺塔：
    首先，n是数量。不管在A、B、C上
    目标1. 把前面n-1从 A-->B
    目标2. 当n=1的时候，从A--->C
    目标3. A的最后一块一定是A-->C 剩下的是n-1 从B-->C

编程思想：a,b,c其实就是移动的位置。a是起始位置，b是过渡位置，c是终点。所以这时候。盘子在哪个上面。哪个就是起始位置。要移动到哪里。那里就是终点。明白动作。
'''
def move(n,a,b,c):
    if(n==1):
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
n=input("Please enter an number : ")
n=int(n)
move(n,'A','B','C')
