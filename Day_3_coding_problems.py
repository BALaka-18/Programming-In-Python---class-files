# abbacccddbj --> a

'''
from collections import Counter

# {'b': 3, 'c': 3, 'a': 2, 'd': 2, 'j': 1}

input_str = input("Enter string : ")

count_dict = Counter(list(input_str))
print(count_dict.most_common(1)[0])
'''

# [1,2,3,4,5,2]

sample_list = [1,2,3,4,5,2]
N = 5
original_sum = (N * (N+1)) // 2
curr_sum = sum(sample_list)

print(curr_sum - original_sum)

# If : consecutive elements from 1 to N, and only 1 element is duplicated.
