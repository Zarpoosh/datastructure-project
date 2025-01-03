import random

def SelectionSort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

lst = random.sample(range(10), 5)
print("Unsorted list:", lst)
sorted_lst = SelectionSort(lst)
print("Sorted list:", sorted_lst)
