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