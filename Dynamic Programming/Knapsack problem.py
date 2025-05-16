def max_value_items(weights,values,n,capacity):
  A=[[0] * (capacity+1) for _ in range(n+1)]
  for i in range(1,n+1):
    for j in range(capacity+1):
       if weights[i - 1] > j:
            A[i][j] = A[i - 1][j]
       else:
            A[i][j] = max(A[i - 1][j], values[i - 1] +A[i - 1][j - weights[i - 1]])
  return A[n][capacity]

weights=[3,1,3,4,2]
values=[2,2,4,5,3]
n=len(weights)
capacity=7
result=max_value_items(weights,values,n,capacity)
print(result)


