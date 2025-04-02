def bubble_sort(array):
    n=len(array)
    print(n)
    
    
    for passes in range(0,n): 
     for j in range(0,n-1):
         if (array[j]>array[j+1]):
             array[j],array[j+1]=array[j+1],array[j]
        
    return array    
        
        
         
    
    
    
    
    
unsorted_list=[83,100,93,17,2,1]
sorted_list=bubble_sort(unsorted_list)
print(sorted_list)
    