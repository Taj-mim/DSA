n1=0
n2=1
n=int(input())
print(n1)
print(n2)
for i in range(n-2): #using loops 
    fib=n1+n2
    print(fib)
    n1=n2
    n2=fib