#6. ** Sum of all elements in a list.**
#- Write a Python function to sum all the elements in a list.
def sum_elements(lst):
    # Your implementation here
    sum = 0
    n =len(lst)-1

    while n >=0:
        sum = sum + lst[n]
        n = n-1
    return sum


print(sum_elements([1, 2, 3, 4, 5]))  # Expected Output: 15
