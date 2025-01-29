#7. ** Check if a number exists in a list.**
#- Write a Python function to check if a specific number exists in the list.
def contains_number(lst, num):
    # Your implementation here
    if num in lst:
        return True
    return False


print(contains_number([1, 2, 3, 4, 5], 3))  # Expected Output: True
print(contains_number([1, 2, 3, 4, 5], 6))  # Expected Output: False
