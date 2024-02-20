# Ex 1
def gen():
    a = int(input('Enter a number: '))
    squares = (i ** 2 for i in range(a))
    for square in squares:
        print(square)

# Ex 2
def gen2(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
even_numbers = gen2(n)
print(",".join(map(str, even_numbers)))  
      
# Ex 3
def gen3(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num
            
n = int(input())
divisible_numbers = gen3(0, n)
print("Numbers divisible by both 3 and 4 between 0 and", n, "are: ")
for num in divisible_numbers:
    print(num, end=", ")
    
# Ex 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a = int(input())
b = int(input())
print(f"Squares from {a} to {b}:")
for square in squares(a, b):
    print(square)
# Ex 5
def gen5(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
print("Countdown from", n, "to 0:")
for num in gen5(n):
    print(num, end=", ")
