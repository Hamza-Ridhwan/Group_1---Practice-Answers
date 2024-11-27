# Write a function that takes a list of numbers and returns a new list with only the unique numbers from the original list.(list methods)


def get_unique_numbers(numbers):
    unique_numbers = [] #Empty list to store unique items
    for num in numbers: 
        if num not in unique_numbers: # Check the numbers on the list
            unique_numbers.append(num) # Used to add new numbers
    return unique_numbers

# Example returning only unique items
numbers = [1, 2, 3, 4, 1, 2, 5, 6]
print(get_unique_numbers(numbers))  


