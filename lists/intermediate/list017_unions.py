# 2. ** Find the union of two lists.**
#- Write a Python function to return a list containing all elements from both lists, without duplicates.

def union_of_lists(lst1, lst2):
   
   return set(lst1) | set(lst2)

# Example usage
lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]

# Call the function and print the result
result = union_of_lists(lst1, lst2)
print(result)
