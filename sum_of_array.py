##recursive approach

def sumarray(l1):
    
    if (len(l1)==0):
        return 0
    else:
        ans= l1[0] + sumarray(l1[1:])
        return ans
    

print(sumarray([1]))




##iterative approach

def sumarray(l1):
    total = 0
    for num in l1:
        total += num
    return total

print(sumarray([]))   
