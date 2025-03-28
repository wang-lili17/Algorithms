def matrix_multiply(A, B): 
    n = len(A) 
    m = len(B[0]) 
    c = [[0] * m for _ in range(n)] 
    for i in range(n): 
        for j in range(m): 
            for k in range(len(B)): 
                c[i][j] += A[i][k] * B[k][j] 
    return c 

A = [ 
    [2, -1, 0], 
    [-1, 2, -1], 
    [0, -1, 2] 
] 

B = [ 
    [2, 1, 4], 
    [1, 2, 1], 
    [4, 1, 2] 
] 

result = matrix_multiply(A, B) 
print(result)
