
from random import choice

new_quates = ['“So many books, so little time.”',
'Two things are infinite: the universe and human stupidity and I am not sure about the universe.”',
'A room without books is like a body without a soul.”',]

def get_quat():
    return '\n'.join(new_quates)

def sure(quate):
    if isinstance(quate , str):
        new_quates.append(quate)
        # print(new_quates)
    else:
        return 'this is not quate'

def cho_quate():
    return choice(new_quates)

if __name__ =='__main__':

    print(get_quat())

    sure('you only live once , but if you do it right . once is enough')
    print('*'*25)
    print(cho_quate())



print('%' *50)
y = [1,2,3,4,5]
if isinstance(y , list):
    print(True)
else:
    print(False)