def twosum(arr,target):
    n=len(arr)

    for i in range(n):
        for j in range(i+1,n):

            if arr[i] + arr[j] == target:
                return True

    return False


array=[1,2,3,4,5]
t=5
ans=twosum(array,t)
print(ans)                
