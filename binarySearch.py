def linearSearch(l,n):
    left=0
    right=len(l)-1
    while(left<=right):
        mid =abs((left+right)//2)
        if(l[mid]==n):
            return mid 
        elif(l[mid]>n):
            right=mid-1
        else:
            left=mid+1
    return -1



l=[1,2,3,4,5]
n=int(input())
print(linearSearch(l,n))