f = open(r'vast.txt', 'w')

f.write('Hello from first page in this file. \n')
f.write('I would like to start with shout out to all of you guys.\n\n')
f.write('First => I could write as well as read in the same time.\n')

f.close()

# f = open('vast.txt', 'r')
# print(f.read())

# f.close()

#=--------------------------------------------------------------------------------------------------------
#------------- Could use this way to open and close the file outomatic ----------------------------------

with open('vast.txt', 'a') as f :
    f.write('Second => Notice this way for writing and reading')
    
with open('vast.txt', 'r') as f :
    print(f.read())


#=--------------------------------------------------------------------------------------------------------
#------------- Notice could handle with two files in the same time and made copy ----------------------------------

with open('vast.txt','r') as f, open('bast.txt','w') as f2:
    line = f.read()                                                           ## COPYING
    f2.write(line)



#============================================================================================================

#======================================&&&  Exception  &&&============================================

#============================================================================================================


# try:
#     with open('error.txt','w') as x:
#         x.write('i love python ')
#         a = 4
#         d = 6 
#         b= (a*d) /2
#         x.write(b)
#         print(' the code has written')
# except :
#     print('could open the file')
# else:
#     print('%% Else %%')

# finally:
#     print('$$ this message always prints $$')

#==============================================================


class TooOldError(Exception):

    def __init__(self,message):
        self.message = message

    def __str__(self):                     ## to print 
        return self.message


class TooYoungError(Exception):

    def __init__(self,message):
        self.message = message

    def __str__(self):
        return self.message

age = int(input('entre your age: '))
if age > 40 : raise TooOldError(f'sorry but {age } is too old try again')
if age < 15 : raise TooYoungError(f'sorry but {age } is too young try again')







