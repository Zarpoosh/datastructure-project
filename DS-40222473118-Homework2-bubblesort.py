import random

def BubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:  
                lst[j], lst[j + 1] = lst[j + 1], lst[j] 

lst = random.sample(range(10), 5)
print("Unsorted list:", lst)
BubbleSort(lst)
print("Sorted list:", lst)
