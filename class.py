class School:
    def __init__(self,name,category,count,teachers,price):
        self.name =name
        self.category =category
        self.count =count
        self.teachers =teachers
        self._price =price     #put under score to price to encapsulate 

    def reduce_price(self,discount):
        self._price =  self._price - self._price*discount

    def set_price(self,price):
        self._price = price


    def full_data(self):
        return f'name {self.name} and caregory {self.category} and count {self.count} and {self.teachers} teachers and the price is {self._price}'

Elryad = School('elryad', 'Arbic', 500, 30,1000)
Dusok = School('usok', 'Franch', 690, 45,2000)
Sidi_salem = School('sidi_salem', 'English', 270, 19,3000)


print(Elryad.count)
print(Sidi_salem.teachers)
print(Dusok.category)
print(Dusok._price)
Dusok.reduce_price(0.10)
print(Elryad.full_data())
print(Dusok._price)

Dusok.price = 0 

print ('ther is no change in price becuase ots producted') 

print(Dusok._price)

#=====================================================================================================
# ------------------- Inheritance---------------------------------------


class Product:
    def __init__(self,name,category,count,teachers,price):
        self.name =name
        self.category =category
        self.count =count
        self.teachers =teachers
        self._price =price

    def reduce_price(self,discount):
        self._price =  self._price - self._price*discount


    def full_data(self):
        return f'name {self.name} and caregory {self.category} and count {self.count} and {self.teachers} teachers and the price is {self._price}'



class Mobile(Product):
    def __init__(self,name,category,count,teachers,price,capacity):
        super().__init__(name, category, count, teachers, price)
        self.capacity = capacity


class Laptop(Product):
    def __init__(self,name,category,count,teachers,price,capacity):
        super().__init__( name, category,count,teachers,price)
        self.capacity = capacity 


Galaxi = Mobile('Galaxi', 'mobile', 400, 30,1000,'23mb')
Iphone = Laptop('Iphone', 'laptop', 690, 45,2000,'55mb')

print(Iphone.full_data())
print(Iphone.count)
print(Galaxi.count)


#=====================================================================================================
# ------------------- Abstract---------------------------------------
# construct method or propertiy inside the class itself

#=====================================================================================================
# ------------------- Inheitance---------------------------------------
from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod

    def area(self):
        print('this is square')

    num = 0

class Square(Shape):
    def __init__(self,side):
        self.side =side
        Shape.num += 1
    def area(self):
        return self.side ** 2

class Cericle(Shape):
    def __init__(self,hights ,width):
        self.hights = hights
        self.width = width
    
    def area(self):
        return (self.hights * self.width)/2
print(Shape.num)
one = Square(4)
two =Cericle(50, 20)
print(one.area())
print(two.area())

print(Shape.num)


#=====================================================================================================
# ------------------- Magic Method---------------------------------------

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z



    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):
        return f' x: {self.x} , y: {self.y} , z: {self.z}'


    def __getitem__(self,key):
        return  self.x[key] 


part = Point('hh','hfh','rer')
part1 =Point(3,8,6)
part2 =Point(5,1,9)
part4 =Point(4,1,3)

part3 = part1 + part2 + part4 

print(part3)


print(part[0])



