# a = 5
# s = int(input('entre your number: '))
# if s == a:
#     print('you win')
# elif s == a+1 or s== a-1:
#     print('you are too close')
# else:
#     print('you lose')

x = 0
# while x < 100:
#     x += 1
#     if x % 2 != 0 : 
#         print(x)
#     else:
#         continue
# else:
#     print('ok')


# for i in range(1,11):
#     for j in range(1,11):
#         print(i * j ,end=' ')
    




# p = int(input('entre your grade' ))
# if p < 50:
#     print ('false')
# elif p >= 50 and p < 60 :
#     print('baleed')
# elif p > 60 and p < 70:
#     print('***')

# elif 71 <= p <= 80:  # <<<<=========
#     print('^^^^^')

# elif p in range(80,91):
#     print('~~@@@@~~')
# else:
#     print('$$$$')


# while True:
#     p = input( 'please entre your name: ')
#     if p =='stop':
#         break
#     else:
#         r = int(input(' entre your age : '))
#         print('hello ', p)
#         print(f'and your age = {2022-r}')





# for i in '*':
#     for l in range(5):
#         print(i * l )
    




num = 1 
for i in range(0,4):
    for j in range(0,i+1):
        print(num , end='')
        num += 1
    print()

print('%'*50)
# =====------ very important  repeatation ------==========

l = [1,2,2,3,4,4,5,6,7,7,8,6]

sas={}

rec = []

for n in l:
    if n not in sas:
        sas[n]='my value'
    else:
        if sas[n] == sas[n]:
            rec .append(n)
print(rec)


print('()'*50)
ert = ['A','B','B','C','D','E','D']
q ={}
w = []

for f in ert:
    if f not in q:
        q[f] = 500
    else:
        if q[f] ==q[f]:
            w.append(f)
print(w)


print('%'* 50)

mm = ['muhamed','ahmed','walled']

# print(len(mm[0]))

d = {}
for p in mm:
    d[p] = len(p)

print(d)

print('%'* 50)

numbers = [1,2,3,4,5,6,7,8,9]
new=[]
size= 3

for b in range(0,len(numbers),size):
    new.append(numbers[b:b+size])
print(new)









difr = [['muhamed','mazen','waleed'] ,'country','age',('one','two','three')]

def k(difr):
    if not difr : return
    if type(difr[0])==list or type(difr[0])==tuple:
        print(k())