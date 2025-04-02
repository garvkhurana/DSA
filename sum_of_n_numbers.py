def sumnumbers(n):
    if (n==1):
        return 1
    else:
        small_ans=sumnumbers(n-1)   
        an=n+small_ans
        return an


print("Enter a number:")
n=int(input())
print(sumnumbers(n))
