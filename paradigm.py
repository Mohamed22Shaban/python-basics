# map

l = [1,2,3,4,5]

def m (l):
    return l**2

b=map(m, l)
print(list(b))

targets = [('cairo',55),('tunss',80),('sudan',60)]

def n (maps):
    return maps[0], (1.8)*maps[1] + 32

g = list(map(n, targets))
print(g)

print(targets[0])


# filter 

p = [('C',1991),('PYTHON',1972),('JAVA',1995),('PHP',1980),('HTML',1990),]

def n (k):
    if k[1] > 1990 :
        return k
h = list(filter(n, p))
print(h)

def n (k):
    if str(k[0]).startswith('P') :
        return k
h = list(filter(n, p))
print(h)

# reduce
from functools import reduce

d = [55,44,24,11]


max_number = reduce(lambda x,y :x if x > y else y , d)
print(max_number)

# comparing

def n (x,y):
    if x > y:
        return x
    else :
        return y
f = reduce(n,d)
