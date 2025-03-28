def insertion_sorting(A):
    
    for j in range(1, len(A)):  
        key = A[j]
        i = j - 1
       
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


input_string = input("Nermucel tarrery anjatelov space ov: ")
A=[]
for element in input_string.split():
    A.append(int(element))
insertion_sorting(A)
print(A)
