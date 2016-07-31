#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import StringIO
from io import BytesIO
'''
f=StringIO()
f.write('Hello ')
f.write('world!')
print(f.getvalue())
'''
f=StringIO('Hello!\nHi!\nGoodBye!')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())

b=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(b.read())
