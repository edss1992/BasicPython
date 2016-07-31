#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

with open('D:\python\BasicPython\\test.txt','w')as f:
    f.write('Today is : ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('D:\python\BasicPython\\test.txt','r')as f:
    s=f.read()
    print('Open for read...')
    print(s)

with open('D:\python\BasicPython\\test.txt','rb')as f:
    s=f.read()
    print('open as binary for read...')
    print(s)
