# 9. ** Merge two lists.**
# - Write a Python function that merges two lists into one.
def merge_lists(lst1, lst2):
    # Your implementation here
    lst1.extend(lst2)
    return lst1


print(merge_lists([1, 2, 3], [4, 5, 6]))  # Expected Output: [1, 2, 3, 4, 5, 6]
