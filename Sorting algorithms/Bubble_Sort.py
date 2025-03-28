def bubble_sort(arr): 

    for i in range(0, len(arr)):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    


arr = [17,8,6,3,9,2,4,98]
bubble_sort(arr)
print(arr)
