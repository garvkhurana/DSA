def stock(arr):
    n=len(arr)
    result=0

    for i in range(n):
        for j in range(i+1,n):
            result=max(result,arr[j] - arr[i])
    return result


array=[1,2,3,4,5]
print(stock(array))           