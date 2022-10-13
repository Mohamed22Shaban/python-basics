l=['mu',['hany','emad','ebraheem'],['cairo','franc','yaman']]

print(l[1][1])
print(l[2][1])

k = ['hany','emad','ebraheem','emad']

k[1] ='hassan'                             #could change for more than index  =<<<<
print(k)
k[0:2] = 'khaled' ,'ramy'
print(k)
print(k.count('emad'))

k.sort()
print(k)
k.extend('dkkdkd')
print(k)
k.insert(1,'dkkdkd')
print(k)

print('$'*50)

a = 'muhammed {}'
b = a.format('shaban')
print(b)

g = ('coordinates {long} ,, {width}'.format(long='32+4j',width='78+1j'))
print(g)

m = 'ramy'
print(f'please call {m}')

p = [1,2,3,4,5]
print(p[:])

print('$'*50)


v= {'one':'muhamed',
'two':'fried',
'tree':'ramy'}
print(v)

v['two'] = 'khalied'
print(v)


print('$'*50)

jj = {'mango','apple','banana','orange'}
# jj['mango'] = 'roman'
print(jj)


print('$'*50)

p = [2,4,5,6]
for i in p :
    o=i*i
print(o)


# الجمع التراكمى
r=[1,2,3,4,6]

o = []
f = 0
for i in r:
    f = f + i
    o.append(f)
print(o)


my_str = 'i love python'
my_list = ['mu',['hany','emad','ebraheem'],['cairo','franc','yaman']]
my_dict = {
    'one':'name',
    'two':'age',
    'three':'number'
}
my_set = {'orange','banana','mango','greepeow','red'}
my_set2 = {'black','red','white','green','orange'}
my_tuples = ( 1,2,3,44,88,99,2)
my_tuples2 = ( 'A','B','C','D')

print(type(my_str))
print(type(my_list))
print(type(my_dict))
print(type(my_set))
print(type(my_tuples))

print(my_str.find('l'))
print(my_str[5])
print(my_str.index('l'))

print('#'*60)

my_list.append('plan')
print(my_list)
my_list.insert(1, 'ramy')
print(my_list)
my_list.extend('kamel')
print(my_list)

print('#'*60)

print(my_dict['two'])
my_dict['two'] = 'five'
print(my_dict)
print(my_dict.items())
print(my_dict.keys())
print(my_dict.get('three'))

print('#'*60)

my_tuples,my_tuples2 = my_tuples2,my_tuples
print(my_tuples)
print(my_tuples2)

print('#'*60)

print(my_set.difference(my_set2))
print(my_set2.difference(my_set))
print(my_set.intersection(my_set2))
print(my_set.union(my_set2))
print(my_set.symmetric_difference(my_set2))
my_set.add('violent')
print(my_set)



