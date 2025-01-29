#5. ** Check if a list is empty.**
#- Write a Python function that returns `True` if the list is empty and `False` otherwise.
def is_empty(lst):
    # Your implementation here
    if not lst:
        return True
    return False


print(is_empty([]))  # Expected Output: True
print(is_empty([1, 2, 3]))  # Expected Output: False
