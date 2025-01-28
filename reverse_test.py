def reverse_list(lst):
    listy = []
    n = len(lst)-1

    while n >= 0:
        listy.append(lst[n])
        n=n-1
    lst =listy
    return lst


print(reverse_list([1, 2, 3, 4, 5]))
    