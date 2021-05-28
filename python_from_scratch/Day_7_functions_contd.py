# FUNCTIONS (contd.)

# Default parameter value
'''
def print_countries(country_user_defined, country_default = "South Korea"):
    print("The name of some countries are : ",country_user_defined, country_default)

# Calling the function
print_countries("India", "Brazil")
print_countries("Bangladesh")
'''

# Return statement
'''
def square_my_num(num):
    new_num = num ** 2
    return new_num



number = 2
new_number = square_my_num(number)
cubed_num = new_number ** 3
print(cubed_num)
'''

# PERFECT NUMBERS :
# WAF to check whether the given number (input) is a perfect number.

def is_perfect(num):
    divisor_sum = 1
    for divisor in range(2,(num//2)+1):
        if num % divisor == 0:
            divisor_sum += divisor

    if divisor_sum == num:
        return "Perfect number"
    else:
        return "Not a perfect number"
    
# Call function for 6, 9, 28
res_6 = is_perfect(num = 6)
res_9 = is_perfect(num = 9)
res_28 = is_perfect(num = 28)

print("For 6 : ",res_6)
print("For 9 : ",res_9)
print("For 28 : ",res_28)
