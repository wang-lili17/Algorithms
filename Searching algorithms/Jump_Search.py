def jump_search(arr, target):
  hop=int(len(arr)**0.5)
  prev=0
  while arr[min(hop,len(arr))-1]<target:
    prev=hop
    hop+=hop
    if prev>=len(arr):
      return 'The element is not in the array'

  for i in range(prev,min(hop,len(arr))):
    if arr[i]==target:
      return i
  return 'The element is not in the array'

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
target = 21
y = jump_search(arr, target)
print(y) 
