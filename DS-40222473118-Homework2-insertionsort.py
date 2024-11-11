import random
def InsertionSort(lst):
    for i in range(1, len(lst)):
        key=lst[i]
        j=i-1
        while j >=0 and key<lst[j]:
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=key
        

lst = random.sample(range(10), 5)
print("Unsorted lst:", lst)
InsertionSort(lst)
print("Sorted lst:", lst)
