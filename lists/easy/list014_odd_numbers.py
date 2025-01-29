# 14. ** Get all odd numbers from a list.**
#- Write a Python function that returns all the odd numbers in a list.
def odd_numbers(lst):
    # Your implementation here
    odd_numbers = []
    for i in lst:
        if i % 2 == 1:
            odd_numbers.append(i)
    return odd_numbers

print(odd_numbers([1, 2, 3, 4, 5, 6]))  # Expected Output: [1, 3, 5]
