# Question : WAF to add all the numbers in a list, without the inbuilt sum() function of Python.

'''
def add_numbers(list_of_nums):
    curr_sum = 0
    for number in list_of_nums:
        curr_sum += number
    print(curr_sum)

# Call the function
nums = [1,2,3,4]
add_numbers(list_of_nums = nums)
'''

# Question : WAF to count all the upper case and lower case characters in a string, and return the individual counts.

'''
def count_chars(input_str):
    upper_count = 0
    lower_count = 0

    for curr_char in input_str:
        if curr_char.isupper():
            upper_count += 1
        elif curr_char.islower():
            lower_count += 1
        else:
            continue
    print("Number of uppercase letters = ", upper_count)
    print("Number of lowercase letters = ", lower_count)

# Call the function
test_string = "BaL@Ka"
count_chars(input_str = test_string)
'''
