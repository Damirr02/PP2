# Ex 1
def ounces(gram):
    print(gram*28.3495231)

ounces(int(input()))

# Ex 2
def centigrade(fahrenheit):
    print((5/9)*(fahrenheit-32))

centigrade(int(input()))

# Ex 3
def solve(numheads, numlegs):
    for chickens in range(numheads+1):
        rabbits=numheads-chickens
        total=2*chickens+4*rabbits
        if total==numlegs:
            print(chickens, rabbits)
        
a=35
b=94
solve(a, b)

# Ex 4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def filter_prime(list):
    for x in list:
        if is_prime(int(x)):
            print(x)
numbers=input().split(" ")
filter_prime(numbers)

# Ex 5
from itertools import permutations

def print_permutations(input_string):
    for perm in permutations(input_string):
        print(''.join(perm))

user_input = input()
print_permutations(user_input)

# Ex 6
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    print(reversed_sentence)

user_input = input()
reverse_words(user_input)

# Ex 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if int(nums[i]) == 3 and int(nums[i + 1]) == 3:
            return True
    return False

numbers = input().split(" ")
print(has_33(numbers))

# Ex 8
def spy_game(nums):
    index = 0
    for num in nums:
        if int(num) == 0 and index == 0:
            index += 1
        elif int(num) == 0 and index == 1:
            index += 1
        elif int(num) == 7 and index == 2:
            return True
    return False
    
numbers=input().split(" ")
print(spy_game(numbers))

# Ex 9
import math
def sphere_volume(radius):
    volume = (4 / 3) * math.pi * radius**3
    print(volume)
    
r=int(input())
sphere_volume(r)

# Ex 10
def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if int(element) not in unique_list:
            unique_list.append(int(element))
    print(unique_list)

elements=input().split(" ")
unique_elements(elements)

# Ex 11
def is_polindrome(word):
    if word == word[::-1]:
        print("True")
    else:
        print("False")
        
is_polindrome(input())

# Ex 12
def histogram(numbers):
    for number in numbers:
        print('*' * int(number))

numbers=input().split(" ")
histogram(numbers)

# Ex 13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    guesses_try = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_try += 1
        
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_try} guesses!")
            break
        
guess_the_number()

