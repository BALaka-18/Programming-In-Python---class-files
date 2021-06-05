# ABSTRACTION
'''

# Library : abc (abstract base class), Class -> ABC (Abstract Base Class)

from abc import ABC

class Car(ABC):
    # Abstract methods have no implementation
    def mileage(self):
        pass

class Maruti(Car):
    # Here, we implement the abstract method mileage
    def mileage(self):
        print("The mileage of this car is 25 kmph")

maruti_obj = Maruti()
maruti_obj.mileage()

'''


# ENCAPSULATION

# Private variables
'''
class Rectangle:
    # Syntax for defining private variables in Python : __<variable name>
    __length = 0
    __breadth = 0

    def __init__(self):
        self.__length = 10
        self.__breadth = 20
        print(self.__length, self.__breadth)


rect_obj = Rectangle()
'''

# Protected variables

class Shape:
    # Syntax for defining protected variables in Python : _<variable name>
    _length = 10
    _breadth = 20

class Rectangle(Shape):
    def __init__(self):
        print(self._length)
        print(self._breadth)

rect_obj = Rectangle()
print(rect_obj.length, rect_obj.breadth)




