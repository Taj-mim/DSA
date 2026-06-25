l=list(map(int,input().split())) #this is for user input
n=len(l)
for i in range(n-1): #as it comares two elements at a time, we need to run the loop n-1 times
    for j in range(n-i-1): #as the last element is already sorted, 
                              #we can reduce the number of comparisons by 1 in each iteration(i) and
                              #   -1 is for it will iterate(n-1) time
        if(l[j]>l[j+1]):
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print("Bubble sort:",l)


#improved version of DSA ----if any array/list is nearly sorted or sorted-------best case time complexity O(n)
#worst case(every element is unsorted) then time complexity is O(n^2) 
#best to use swaapped for any kind of array
l=list(map(int,input().split()))
n=len(l)

for i in range(n-1):
    swapped=False
    for j in range(n-i-1):
        if(l[j]>l[j+1]):
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
            swapped=True
        if not swapped:
            break
print("Using swapped flag for improving bubble sort:",l)