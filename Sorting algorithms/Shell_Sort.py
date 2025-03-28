def shell_sort(arr):
    gap = len(arr) // 2  

    # insertion sort for this gap
    while gap > 0:

        for i in range(gap, len(arr)):
            
            k = arr[i]
            j = i

            
            while j >= gap and arr[j - gap] > k:
                arr[j] = arr[j - gap]
                j -= gap

            
            arr[j] = k
        
        gap //= 2


arr = [17,8,6,3,9,2,4,98]
shell_sort(arr)
print(arr)
