
def factorial(n):
    if n==1:
        return 1
    else:
        answer=n*factorial(n-1)
        return answer
    
    

print(factorial(10))


# here the functional factorial is calling it self and then it is returning the answer and then it is multiplying the answer with
# the number and then it is returning the answer
