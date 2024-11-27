# Implement a function that takes a list and returns True if the list is sorted in ascending order, otherwise False


# Solution one
def is_sorted (numbers):
    return numbers == sorted(numbers)
print(is_sorted([9, 2, 3]))
print(is_sorted([3, 2, 1]))

# Solution two

def is_sorted (numbers):
    if numbers == sorted(numbers):
        return True
    else:
        return False

print(is_sorted([9, 3, 5]))    