n1=0
n2=1
n=int(input())
print(n1)
print(n2)
for i in range(n-2): #using loops is the best approach for 
                        #fibonacci as it takes O(n) time complexity and O(1) space complexity 
    fib=n1+n2
    print(fib)
    n1=n2
    n2=fib

"""tabulation method for fibonacci series
def fibo(n):
    f=[0]*(n+1) #creating a list of size n+1 and initializing all values to 0
    f[0]=0
    f[1]=1
    for i in range(2,n+1):
        f[i]=f[i-1]+f[i-2]
    return f[n]"""