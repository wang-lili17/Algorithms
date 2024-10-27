'''the code is still in progress'''

import math
def appropriate(A,B):
    rows, cols = len(A), len(A[0])
    rows2, cols2 = len(B), len(B[0])
    if not (rows == cols and math.log2(rows).is_integer()) or not (rows2 == cols2 and math.log2(rows2).is_integer()):
        return False
    return True



def matrix_multiply(A, B):
  
    if not appropriate(A,B):
        print("Matrices must be square and power of 2")

    n = len(A)

    
    if n <= 2:
        return multiply_2x2(A, B)

    
    mid = n // 2
    A11, A12, A21, A22 = split_matrix(A, mid)
    B11, B12, B21, B22 = split_matrix(B, mid)

    
    C11 = matrix_multiply(A11, B11) + matrix_multiply(A12, B21)
    C12 = matrix_multiply(A11, B12) + matrix_multiply(A12, B22)
    C21 = matrix_multiply(A21, B11) + matrix_multiply(A22, B21)
    C22 = matrix_multiply(A21, B12) + matrix_multiply(A22, B22)

    
    return combine_matrices(C11, C12, C21, C22)


def multiply_2x2(A, B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]


def split_matrix(matrix, mid):
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]


    return A11, A12, A21, B11, B12, B21, B22

def combine_matrices(C11, C12, C21, C22):

    return [left + right for left, right in zip(C11 + C21, C12 + C22)]

A = [[1, 5], [7, 4]]
B = [[5, 9], [7, 11]]

result = matrix_multiply(A, B)
print(result)
