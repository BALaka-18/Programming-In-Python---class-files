# Inheritance

# BASIC SYNTAX
'''
# Parent class / Superclass
class Animal:
    def speak(self):
        print("This animal is communicating")
# Child class / Subclass
class Dog(Animal):
    def bark(self):
        print("This dog can bark")

# Call the object

dog_obj = Dog()
dog_obj.bark()
dog_obj.speak()
'''

# MULTI-LEVEL INHERITANCE
'''
class Animal:
    def speak(self):
        print("This animal is communicating")

# Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        print("This dog can bark")

# Puppy inherits from Dog
class Puppy(Dog):
    def is_child(self):
        print("This animal is a child of dog")

puppy_obj = Puppy()
puppy_obj.is_child()
puppy_obj.bark()
puppy_obj.speak()
'''

# MULTIPLE INHERITANCE
class Calc_Sum:
    def summation(self, num1, num2):
        return num1 + num2
class Calc_Pdt:
    def multiply(self, num1, num2):
        return num1 * num2

class Child_class(Calc_Sum,Calc_Pdt):
    def divide(self, num1, num2):
        return num1 / num2

div_obj = Child_class()
num1 = int(input())
num2 = int(input())

print(div_obj.summation(num1, num2))
print(div_obj.multiply(num1, num2))
print(div_obj.divide(num1, num2))

















