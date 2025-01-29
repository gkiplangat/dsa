# **Find the intersection of two lists.**
# - Write a Python function to find the common elements between two lists.

def list_intersection(lst1, lst2):
    comon = []

    for i in (set(lst1) & set(lst2)):
            comon.append(i)
    return comon

listy1 = [1, 2, 3, 4, 5]
listy2 = [3, 4, 5, 6, 7]

result = list_intersection(listy1, listy2)
print("Intersection of the two lists:", result)
