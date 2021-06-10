# POLYMORPHISM

'''
# Vegetable class
class Lettuce:
    def type(self):
        print("This is a vegetable")
    def color(self):
        print("Green")

# Fruit class
class Apple:
    def type(self):
        print("This is a fruit")
    def color(self):
        print("Red")

# Function to utilize both classes and show how polymorphism in OOP differs them successfully
def func(obj):
    obj.type()
    obj.color()

# Driver code
veg_obj = Lettuce()
fruit_obj = Apple()
# Call func() for both the objects
func(veg_obj)
func(fruit_obj)
'''


# POLYMORPHISM WITH INHERITANCE

'''
# Parent : Bird
class Bird:
    def defn(self):
        print("This is a test string for the parent class, Bird")
    def flight(self):
        print("This is a test string for the parent class, Bird")

# Define child classes
class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly")
class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly")


bird_obj = Bird()
sparrow_obj = Sparrow()
ostrich_obj = Ostrich()

bird_obj.flight()
sparrow_obj.flight()
ostrich_obj.flight()
'''








































































