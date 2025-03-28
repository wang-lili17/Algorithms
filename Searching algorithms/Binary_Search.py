def binary_search(arr, target):
    if len(arr) == 0:
        return 'The element is not in the array'
    mid = len(arr) // 2  

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        result = binary_search(arr[:mid], target)
        return result
    elif arr[mid] < target:
        result = binary_search(arr[mid + 1:], target)
        return result+mid+1
    else:
        return 'The element is not in the array'

arr = [2, 5, 6, 7, 8, 9, 10, 40, 100]  
target = 10
y = binary_search(arr, target)
print(y)
