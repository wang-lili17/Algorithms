def selection_sort(tver): 
    for i in range(len(tver)): 
        min_idx = i 
        for j in range(i+1, len(tver)): 
            if tver[j] < tver[min_idx]: 
                min_idx = j 
 
        tver[i], tver[min_idx] = tver[min_idx], tver[i] 
 
    return tver 
 
tver= [5, 25, 15, 22, 11] 
sortavorvac_tver = selection_sort(tver) 
print("Sorted numbers:", sortavorvac_tver)
