
#11. ** Get the second-largest element in a list.**
#- Write a Python function to return the second-largest number in a list.
def second_largest(lst):
    # Your implementation here
    n = len(lst)-1
    sorted = 0
    for i in range(n):
        if lst[i] > lst[i+1]:
            

    return sorted


print(second_largest([1, 2, 3, 4, 5]))  # Expected Output: 4
