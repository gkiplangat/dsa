
#11. ** Get the second-largest element in a list.**
#- Write a Python function to return the second-largest number in a list.
def second_largest(lst):
    # Your implementation here
    sorted = lst.sort()
    return lst[-2]


print(second_largest([1, 2, 3, 4, 5]))  # Expected Output: 4
