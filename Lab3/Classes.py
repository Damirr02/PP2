import math
# Ex 1

class upperString:
    def __init__ (self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")
    
    def printString(self):
        print(self.input_string.upper())


# Ex 2
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length * self.length
    
# Ex 3
class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length
    def area(self):
        return self.length * self.width 


# Ex 4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# Ex 5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, number):
        self.balance += number
    def withdraw(self, number):
        if self.balance < number:
            return "can't withdraw"
        self.balance -= number


# Ex 6
def isPrime(num):
    if int(num) < 2:
        return False
    for i in range(2, int(int(num)**0.5 + 1)):
        if int(num) % i == 0:
            return False
    return True

numbers = input().split(" ")
prime_numbers = list(filter(lambda x: isPrime(x), numbers))
prime_numbers = list(map(int, prime_numbers))
print(prime_numbers)

