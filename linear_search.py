def linear_search(array,target):
    size=len(array)
    for i in range(0,size):
        if array[i]==target:
            return i
        
    return -1



my_list=[1,2,3,4,5,6,7,8,9,10]
target=100

result=linear_search(my_list,target)
print(result)  
        