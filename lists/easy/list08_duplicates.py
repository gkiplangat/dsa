
#8. ** Remove duplicates from a list.**
#- Write a Python function to remove duplicate values from a list.
def remove_duplicates(lst):
    # Your implementation here
    check_duplicate = set()
    for i in lst:
        check_duplicate.add(i)
    return check_duplicate


print(remove_duplicates([1, 2, 2, 3, 3, 4]))  # Expected Output: [1, 2, 3, 4]
