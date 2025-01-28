# 1. ** Reverse a list.**
#- Write a Python function to reverse a list without using the `reverse()` function.

def reverse_list(lst):
    # Your implementation here
    return lst[::-1]


print(reverse_list([1, 2, 3, 4, 5]))  # Expected Output: [5, 4, 3, 2, 1]
