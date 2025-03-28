def ternary_search(arr, target):
    if len(arr) == 0:
        return 'The element is not in the array'
    mid1 = len(arr) // 3  
    mid2 = 2 * len(arr) // 3
    if arr[mid1] == target:
        return mid1
    elif arr[mid2] == target:
        return mid2

    elif arr[mid1] > target:
        result = ternary_search(arr[:mid1], target)
        return result
    elif arr[mid1] < target and arr[mid2]>target:
        result = ternary_search(arr[mid1 + 1:mid2], target)
        return result+mid1+1
    elif arr[mid2] < target and target<=arr[-1]:
        result = ternary_search(arr[mid2 + 1:], target)
        return result+mid2+1
    else:
        return 'The element is not in the array'

arr = [2, 5, 6, 7, 8, 9, 10, 40, 100]  
target = 101
y = ternary_search(arr, target)
print(y)
