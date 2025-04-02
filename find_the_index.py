def findindex(arr,x):
    if (len(arr)==0):
        return -1
    elif (arr[0]==x):
        return 0
    
    else:
    
      answer= findindex(arr[1:],x) 
    return answer + 1 if answer != -1 else -1
      
        
    
    
array=[1,2,3,4,5]    
index=findindex(array,10) 
print(index)   