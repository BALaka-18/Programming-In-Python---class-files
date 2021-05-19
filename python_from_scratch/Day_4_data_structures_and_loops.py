# Stack

'''
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
tos = stack.pop()
print(tos)
print(stack)
'''

# Queue

'''
1.
from queue import Queue

queue1 = Queue()
queue1.put(1)
queue1.put(2)
queue1.put(3)

print(queue1.get())
'''

'''
2.
from collections import deque

q2 = deque()
q2.append(1)
q2.append(2)
q2.append(3)

print(q2.popleft())
'''


# Flow of control statements

# 1. FOR LOOP

# Basic syntax : for <iterator> in range(start, stop + 1, jump)
# for <iterator> in <iterable>

string_1 = "abcadacbasra"
for letter in string_1:
    if letter is 'a':
        print(letter)
    else:
        continue
