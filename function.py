
print(' positional argument')
def data(company , country):
    print(company , country)

data('BGB', 'Egypt')

print('&'*50)
print(' keyword argument')

def data(company , country):
    print(company , country)

data(country='BGB',company='Egypt')

print('&'*50)

def info(name, age, wight):
    print(f'Name: {name} ,,  Age: {age} ,, and {wight} kg ')

# info('muhammed', 31, wight=80)


def info(name,  wight,age=50):
    print(f'Name: {name} ,,  Age: {age} ,, and {wight} kg ')

info('muhammed',80)


print('&'*50)

def bob(*fruits):
    for fruit in fruits:
        print(f'i like {fruit}')

bob('apple','banana','watermelon','mango')


print('&'*50)

def my_dict(**names):
    for name ,nn in names.items():
        print(f'i like {name} => {nn}')

my_dict(one='muhamed',two='abderhamn' , three='roushdy', four='glal')


def outer():
    x = 50
    def inner():
        x = 100
        print(x)
    inner()
outer()

def outer():
    x = 50
    print( x)
    def inner():
        nonlocal x
        x = 100
        print(x)
    inner()
outer()

print('&'*50)

gg =lambda a:a+2
print(gg(5))


fun_name = lambda pramter_one , pramter_two : f' my name {pramter_one } {pramter_two}'
print(fun_name('muhammed ','shaban'))

print('&'*50)

#=======================================================================================

my_list = ['id11', 'id6','id55','id22','id2','id5','id4']
my_list.sort(key=lambda x :int(x[2:]))
print(my_list)

print('&'*50)

def num (a):
    if a == 1 :
        return a
    else:
        return a* num(a-1)
print(num(5))

print('&'*50)
#=======================================================================================


difr = [['muhamed','mazen','waleed'] ,'country','age',('one','two','three')]
def info(difr):
    if not difr: return
    if (type(difr[0]) == list or type(difr[0]) == tuple):
        info(difr[0])
    else:
        print(difr[0])
    info(difr[1:])
info(difr)

#=======================================================================================



print('&'*50)
def gener(numbers):
    for number in range(1,numbers,2):
        yield number
def fener (nums):
    for numbe in nums:
        yield numbe ** 2
print(sum(fener(gener(10))))
#=======================================================================================



odd  =( number for number in range(1, 10 ,2) )

cdd  =( number**2 for number in odd )
print(sum(cdd))

