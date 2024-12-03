# Question 4
# Create a Python program that calculates the maximum value among 5 numbers entered by the user. The program should:
# Prompt the user to enter 5 numbers one by one through the terminal.
# Find and display the maximum value among the entered numbers.
# Ensure the input is numeric and handle invalid inputs gracefully (e.g., prompt the user again if a non-numeric value is entered).
# Example 
# Enter number 1: 12
# Enter number 2: 45
# Enter number 3: 7
# Enter number 4: 89
# Enter number 5: 34
# The maximum value is: 89

# Hints:
# Use a loop to collect the inputs.
# Store the numbers in a list i.e using append
# Use Python's max() function or implement logic to find the maximum.

max()
#input()

#int()

#range()

def max_number():              #try-except block
    number=[]
    for i in range(1, 6):
        while True:
            try:
                num = float((input(f"Enter a number {i}: ")))
                number.append(num)
                break
            except ValueError:
                print("Invalid number")
    print(f"maximun number is : {max(number)}")   #max()
max_number()

