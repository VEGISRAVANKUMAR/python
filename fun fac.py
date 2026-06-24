def Factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    print(result)
n=int(input())
Factorial(n)