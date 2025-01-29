#4. ** Find the minimum element in a list.**
#- Write a Python function to find the smallest number in a list.
def find_min(lst):
    # Your implementation here
    if not lst:
        raise ValueError("List is Empty")
    return min(lst)


print(find_min([1, 2, 3, 4, 5]))  # Expected Output: 1
