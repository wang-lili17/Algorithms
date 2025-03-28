def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    else:
        return ('the element is not in the array')

arr = [2, 5, 6, 7, 9, 8, 4, 1]
target = 9
y = linear_search(arr, target)
print(y)
