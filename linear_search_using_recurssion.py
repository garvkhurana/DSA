def linearsearch(arr,x,index):
    if(len(arr)==0):
        return -1
    
    elif(len(arr)==index):
        return -1
    
    elif arr[index] == x:
        return index    
    
    else:
        answer=linearsearch(arr,x,index+1)
        
    return answer    


array=[1,2,3,4,5]
ans=linearsearch(array,5,0)
print(ans)