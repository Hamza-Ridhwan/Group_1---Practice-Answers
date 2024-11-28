# Write a Python program to print all numbers between two user-provided integers, skipping numbers divisible by 7.

num1 = int(input('Enter number 1:'))
num2 = int(input('Enter number 2:'))

for num in range(num1, num2):
    if num % 7 != 0:
        print(num)