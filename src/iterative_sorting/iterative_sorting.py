# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        min_idx = i 
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for c in range(i + 1, len(arr)):
            if arr[min_idx] > arr[c]:
                min_idx = c
        
        arr[i] , arr[min_idx] = arr[min_idx], arr[i]



        # TO-DO: swap
        # Your code here

    return arr

list = [3,4,2,3,1]
print(selection_sort(list))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swaps = 1

    while swaps > 0:
        swaps = 0
        for i in range(0, len(arr) -1):
            if arr[i] > arr[i + 1]:
                swaps += 1 
                arr[i], arr[i+1] = arr[i+1], arr[i]


    return arr


list = [3,4,2,3,1]
print(bubble_sort(list))
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here

    if not maximum:
        maximum = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > maximum:
                maximum = arr[i]

    buckets = [0] * (maximum + 1)

    for i in range(0, len(arr)):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"
        buckets[arr[i]] += 1

    arr = []
    [arr.extend([i] * x) for i, x in enumerate(buckets) if x > 0]

    return arr

                var = 1    
list = [3,4,2,3,1]
print(counting_sort(list))