# Basic loop 0-9 prints out numbers 0 through 9
'''
for i in range(10):
    print(i)
'''

# Loop with condition that is always false - will not run
'''
for i in range(200, 10):
    print(i)
'''
    
# Infinite loop example - commented out for saftey
# Loop would run forever because condition is always true

# while True:
#     print(i)

# Using step parameter to print even numbers between 0-100
'''
for i in range(0, 101, 2):
    print(i)
'''

# While loop printing even numbers 0-100
'''
i = 0
while i <= 100:
    print(i)
    i += 2
'''  

## Challenge 1
# Print all the numbers from 1 to 100 (inclusive), while skipping the numbers from 50 to 60.

# Basic loop 1-100
'''
for i in range(1, 101):
    print(i)
'''
    
# Loop 1-100 skipping 50-60
'''
for i in range(1, 101):
    if 50 <= i <= 60:
        continue
    print(i)
'''

# While loop 1-100
'''
i = 1
while i <= 100:
    print(i)
    i += 1
'''

# While loop 1-100 skipping 50-60
'''
i = 1
while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue
    print(i)
    i += 1
'''

# Do-while loop implementation in python

# Loop 1-100 skipping 50-60 using do-while pattern
'''
i = 1
while True:
    if i > 100:
        break
    if 50 <= i <= 60:
        i += 1
        continue
    print(i)
    i += 1
'''
## Challenge 2
# Loop thorugh all the numbers 1 to 100 (inclusive) and print specific messages for multiples of 3, 5, and 3 & 5.
# Common interview challenge: Missing Link

# - If the number is a multiple of 3, print "Fizz"
# - If the number is a multiple of 5, print "Buzz"
# - If the number is a multiple of 3 and 5, print "FizzBuzz"
# - Use the modulo operator (%) to check if a number is a multiple of another number

'''
for i in range(0, 101):
    if i % 3 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
'''

 # Generator expression creating squares 0-4
'''
squares = (x * x for x in range(5))
print(f"Generator of squares: {squares}")
print(f"Values from generator: {list(squares)}")
'''

# Generator vs list comprehension comparison
'''
even_gen = (x for x in range(10) if x % 2 == 0)
even_list = [x for x in range(10) if x % 2 == 0]

print(f"\nGenerator values: {list(even_gen)}")
print(f"List values: {even_list}")
'''

# Generator expression in for loop
'''
print("\nIterating through generator: ")
names = (f"Hello {name}" for name in ["Alice", "Bob", "Charlie"])
for greeting in names:
    print(greeting)
'''

# Checking for number greater than 5
'''
numbers = [1, 3, 7, 2, 4]
result = any(num > 5 for num in numbers)
print(f"\nIs any number greater that 5? {result}\n")
'''

# Checking for letter "a" in strings
'''
words = ["hello", "world", "python"]
result = any("a" in word for word in words)
print(f"\nDoes any word contain 'a' ? {result}\n")
'''

# Checking for True value
'''
values = [False, False, True, False]
result = any(values)
print(f"Is any value True? {result}")
'''

## Challenge 3
# - Use a loop to traverse through the numbers array
# - Print "Yes" if the array contains at least on even number
# - Print "No" otherwise

numbers = [33, 39, 11, 99, 101, 89, 45, 51, 32, 44]
has_even_number = any(number % 2 == 0 for number in numbers)
print("Yes" if has_even_number else "No")