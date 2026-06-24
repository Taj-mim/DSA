#for nth term value of fibonacci series using recursion
def fibo(n):
    if n<=1:       #time complexity O(2^n) and space complexity is O(n)
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input())
print(fibo(n))