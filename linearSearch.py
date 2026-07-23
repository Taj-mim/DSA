def linearSearch(l,n):
    for i in range(len(l)):
        if(l[i]==n):
            return i

    return -1


l=[1,2,3,4,5]
n=int(input())
print(linearSearch(l,n))