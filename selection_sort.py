def selection_sort(arr):
    n=len(arr)
    min_index=0
    
    for j in range(1,n):
        if (arr[j] < arr[min_index]):
            min_index=j
            
    arr[0],arr[min_index]=arr[min_index],arr[0]
    return arr
    
unsorted_list=[80,40,1,22,41]
sorted_list=selection_sort(unsorted_list)
print(sorted_list)    
            