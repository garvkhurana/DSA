def secondlargest(arr):
    first_max=arr[0]
    for i in range(0,len(arr)):
        if (first_max<arr[i]):
            return first_max 
        
    array2=[x for x in arr if x != first_max] 
    max2=array2[0]
    for i in range (0,len(arr)):
        if (max2<arr[i]):
            return max2
        


if __name__=="__main__":
    array=[1,2,3,4,5]
    max=secondlargest(array)
    print(max)        
        
        
            