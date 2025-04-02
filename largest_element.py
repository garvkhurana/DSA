def largestelement(arr):
    
    max=arr[0]
    for i in range(0,len(arr)):
        if (max < arr[i]):
            max=arr[i]
    return max


if __name__=="__main__":
    array=[1,2,3,4,5]
    max=largestelement(array) 
    print(max)       
        