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