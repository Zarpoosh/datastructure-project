import time
import random

def InsertionSort(lst):
    for i in range(1, len(lst)):
        key=lst[i]
        j=i-1
        while j >=0 and key<lst[j]:
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=key
   
   
   

def SelectionSort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    
        

def BubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:  
                lst[j], lst[j + 1] = lst[j + 1], lst[j] 

lst = random.sample(range(10), 5)
print("Unsorted lst:", lst)

start_time1 = time.time()
InsertionSort(lst)
end_time1 = time.time()

start_time2 = time.time()
SelectionSort(lst)
end_time2 = time.time()

start_time3 = time.time()
BubbleSort(lst)
end_time3 = time.time()

print("Sorted lst:", lst)
execution_time1 = end_time1 - start_time1
execution_time2 = end_time2 - start_time2
execution_time3 = end_time3 - start_time3
print("Execution InsertionSort:", execution_time1, "seconds")
print("Execution SelectionSort:", execution_time2, "seconds")
print("Execution BubbleSort:", execution_time3, "seconds")