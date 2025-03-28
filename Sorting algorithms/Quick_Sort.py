def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr

   
    pivot = arr[-1]

    
    left = [x for x in arr[:-1] if x <= pivot]  
    right = [x for x in arr[:-1] if x > pivot]  
    
    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)

    
    return left_sorted + [pivot] + right_sorted

arr = [1, 8, 3, 9, 4, 5, 7, 6, 2, 0]
sorted_arr = quick_sort(arr)
print( sorted_arr)
