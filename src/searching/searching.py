def linear_search(arr, target):
    # Your code here
    searchArr = arr.copy()
    currTarget = searchArr.pop(0)
    
    while len(searchArr) > 1:
        if currTarget == target:
            return currTarget
        
        currTarget = searchArr.pop(0)


    return -1   # not found

list = [x for x in range (1,51)]
# print(list)

# print(linear_search(list, 6))
# print(linear_search(list, 1))
# print(linear_search(list, 3))
# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    searchArr = arr.copy()
    currentTarget = searchArr[len(searchArr) //2 ]

    while len(searchArr) > 0:
        print(searchArr, "Sea")
        if currentTarget == target:
            return currentTarget
        elif len(searchArr) == 1 and currentTarget != target:
            return -1 
        elif currentTarget > target:
            searchArr = searchArr[0 : (len(searchArr) //2)]
        elif currentTarget < target:
            searchArr = searchArr[ (len(searchArr) //2 + 1) : len(searchArr)]

        if len(searchArr) > 0:
            currentTarget = searchArr[len(searchArr) //2 ]
    
    return -1 


[print(binary_search(list, x)) for x in list]
print(binary_search(list, 51))