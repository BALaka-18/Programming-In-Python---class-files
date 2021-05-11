'''
Q.1. Anagrams


# earth -> heart
# listen -> silent

# Sort 'earth' -> a,e,h,r,t
# Sort 'heart' -> a,e,h,r,t

string1 = "like"
string2 = "kale"

if sorted(string1) == sorted(string2):
    print("Anagram")
else:
    print("Not an anagram")

'''

'''
Palindrome
'''

# racecar -> racecar
# abba -> abba

string1 = "acba"

start,end = 0,len(string1)-1
flag = True

while start <= end:
    if string1[start] == string1[end]:
        start += 1
        end -= 1
    else:
        flag = False
        break

if flag:
    print("Palindrome")
else:
    print("Not a Plaindrome")
