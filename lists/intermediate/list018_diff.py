#3. ** Find the difference between two lists.**
# - Write a Python function to return the elements that are in the first list but not in the second.
def difference_of_lists(lst1, lst2):
    unique =set()
    for i in lst1:
        if i not in lst2:
            unique.add(i)
    return unique
    


# Example usage
lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 6]

# Call the function and print the result
result = difference_of_lists(lst1, lst2)
print(result)  # Expected output: [1, 2, 5]
