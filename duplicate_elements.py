def repeat(arr):
    n=len(arr)
    freq= [0] * 1
    result=[]

    for num in arr:
        freq[num] += 1


    for i in range(n):
        if freq[arr]>1:
            result.append(i) 

        else:
            result.append(-1)

    return result

array=[1,1,2,3,3,4,5,6,6]   
print(repeat(array))        









