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

'''
numbers = [33, 39, 11, 99, 101, 89, 45, 51, 32, 44]
has_even_number = any(number % 2 == 0 for number in numbers)
print("Yes" if has_even_number else "No")
'''

# Sum of numbers demonstration
'''
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"Sum of numbers: {total}")
'''

'''
# Sum of Squares 0-3
total_squares = sum(x * x for x in range(4))
print(f"Sum of squares: {total_squares}")
'''
## Challenge 4

# - Use a loop that will traverse through the numbers array
# - Count the total number of even numbers
# - Print it to the console
'''
numbers = [33, 39, 11, 99, 101, 89, 45, 51, 32, 44]
number_of_even_numbers = sum(1 for number in numbers if number % 2 == 0)
print(number_of_even_numbers)
'''

## Challenge 5 
# - Use a loop to go through all of the letters in a string
# - Count the number of spaces and print the number of spaces in the string

'''
message = "I love to eat apples and bananas for breakfast."
number_of_spaces = sum(1 for char in message if char == " ")
print(number_of_spaces)
'''

## Challeneg 6
# Given a list of numbers, perform various calculations
array = [13, 35, 54, 81, 103, 76, 1, 54, 17, 99]

# - Find the sum of all numbers
sum_of_all_numbers = sum(array)
print(sum_of_all_numbers)

# - Find the average of all numbers
average_of_all_numbers = sum(array) / len(array)
print(average_of_all_numbers)

# -  Find the maximum and minimum numbers
max_number = max(array)
print(max_number)
min_number = min(array)
print(min_number)

# - Find the sum of all even numbers
sum_of_all_even_numbers = sum(x for x in array if x % 2 == 0)
print(sum_of_all_even_numbers)

# - Find average of all odd numbers
odd_number = [x for x in array if x % 2 != 0]
average_odd = sum(odd_number) / len(odd_number) if odd_number else 0
print(average_odd)