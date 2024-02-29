from functools import reduce
import operator
import time
import math

# Ex 1
def multiply_list(numbers):
    if not numbers:
        return None
    return reduce(operator.mul, numbers)

if __name__ == "__main__":
    numbers = input().split()
    numbers = [int(num) for num in numbers]
    result = multiply_list(numbers)
    print(result)
    
# Ex 2
def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

if __name__ == "__main__":
    input_string = input()
    upper_count, lower_count = count_upper_lower(input_string)
    print(upper_count)
    print(lower_count)
    
# Ex 3
def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

if __name__ == "__main__":
    input_string = input()
    if is_palindrome(input_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
    
# Ex 4
def calculate_square_root(num, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(num)
    print(f"Square root of {num} after {milliseconds} milliseconds is {result}")

if __name__ == "__main__":
    num = int(input("Input: "))
    milliseconds = int(input())
    calculate_square_root(num, milliseconds)
    
# Ex 5
def all_true(t):
    return all(t)

if __name__ == "__main__":
    my_tuple = (True, True, True, True)
    if all_true(my_tuple):
        print("True")
    else:
        print("False")