#13. ** Get all even numbers from a list.**
#- Write a Python function that returns all the even numbers in a list.

def even_numbers(lst):
    # Your implementation here
    even_numbers = []

    for i in lst:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers
print(even_numbers([1, 2, 3, 4, 5, 6]))  # Expected Output: [2, 4, 6]
