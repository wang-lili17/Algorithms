def merge_sort(arr):
    if len(arr)<=1:
        return arr


    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left=merge_sort(left)
    right=merge_sort(right)

    return merge(left,right)

def merge(left,right):
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    while i<len(left):
        result.append(left[i])
        i+=1

    while j<len(right):
        result.append(right[j])
        j+=1
    return result


arr = [17,8,6,3,9,2,4,98]
sorted_arr=merge_sort(arr)
print(sorted_arr)
