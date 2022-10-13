from datetime import date

d = date(2022 , 5 , 18)
print(d)

c = date.today()
print(c)

f = d - c
print(f)

s = d.strftime(' %A: %Y %B %d')
print(s)

#=====================================================================================

from datetime import time

x = time(hour=12,minute=25,second=50)
print(x)

#=====================================================================================

from datetime import datetime

o = datetime(year=2022,month=11,day=15,hour=2,minute=15,second=55)
print(o)

l = datetime.now()
print(l)


#=====================================================================================

import decimal

print(decimal.Decimal(4))
print(decimal.Decimal('2.15'))


#=====================================================================================

import random

l = ['muhammed','hussam','waleed','fathy']
print(random.random())
print(random.randint(1, 10))
print(random.choice(l))
print(random.choices(l , k=2))
print(random.randrange(10))

print(l)
random.shuffle(l)
print(l)


import sys

print(sys.platform)
print(sys.getwindowsversion())
print(sys.version)


import os
print(os.getcwd())
os.chdir('my_packages')
print(os.getcwd())
os.chdir('..')
print(os.listdir('my_packages'))
os.mkdir('lll')

import shutil


