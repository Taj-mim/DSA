l=list(map(int,input().split(',')))
n=len(l)
for i in range(n-1):
    index_start=i
    for j in range(i+1,n):
        if(l[j]<l[index_start]):
            index_start=j
        temp=l[i]
        l[i]=l[index_start]
        l[index_start]=temp
print(l)

#this is the best way we can also use shifting.but shifting takes more time for that using swapping is best
