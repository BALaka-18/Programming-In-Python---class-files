# filter
# [1,2,3,4,5] --> [2,4]

'''
raw_list = [1,2,3,4,5]
even_list = list(filter(lambda x: x % 2 == 0, raw_list))
print(even_list)
'''

# map
# [1,2,3,4,5] --> [3,6,9,12,15]

'''
raw_list = [1,2,3,4,5]
prod_list = list(map(lambda x: x * 3, raw_list))
print(prod_list)
'''

# import <library_name> --> <library_name>.<function_name>(...)
# from <library_name> import <function_name>

'''
from functools import reduce

raw_list = [1,2,3,4]
product = reduce(lambda x,y: x * y, raw_list)
print(product)
'''

set1 = set()
print(type(set1))
