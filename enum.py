#!/usr/bin/env python
#-*-coding:utf-8-*-
from enum import Enum, unique
@unique
class weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6
day1=weekday.Mon

print('day1=',day1)
print('weekday.Tue=',weekday.Tue)
print('day1==weekday.Mon?',day1==weekday.Mon)
print('day1==weekday(1)?',day1==weekday(1))

for name, member in weekday.__members__.items():
    print(name,'==>',member)
