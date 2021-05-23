# Functions - def <function_name>(N):

'''
# Defining a function
def print_name(name1,name2):
    print(name1,name2)

# Calling the function
print_name(name1 = "Ashish",name2 = "xyz")
print_name("Ashish","xyz")
# Error
# print_name()
print_name("Ashish")
'''

'''
# *args-
# Definition
def test_function(*args):
    print(args[1])
# Calling
test_function("a","b","c","d","e","f")
# What actually happens
def test_function(("a","b","c","d","e","f")):
    print(args[1])
'''

def test_kwargs(**kwargs):
    print("My last name is : ", kwargs["lname"])

test_kwargs(fname = "Ashish", lname = "Kumar")


def test_kwargs(kwargs = {"fname" : "Ashish", "lname" : "Kumar"}):
