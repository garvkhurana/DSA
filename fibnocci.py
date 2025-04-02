import sys
sys.setrecursionlimit(1000)



def fibnocci(n):
    print(n)
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        last_num=fibnocci(n-1)
        second_last_num=fibnocci(n-2)
        an=last_num+second_last_num
        return an

print("Enter a number:")
n=int(input())
print(fibnocci(n))
