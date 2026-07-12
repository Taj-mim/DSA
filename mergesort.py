
def merge(arr,start,mid,end):
    temp =[] #to store the value before mergeing last left and right side
    i=start
    j=mid+1
    while(i<=mid and j<=end): #check left value with right side value
        if(arr[i]<=arr[j]):  
            temp.append(arr[i])
            i=i+1
        else:
            temp.append(arr[j])
            j=j+1
    while(i<=mid): #adds remaining left elements into temporary list.
         temp.append(arr[i])
         i=i+1
    while(j<=end):#adds remaining right elements into temporary list.
        temp.append(arr[j])
        j=j+1

    for indx in range(len(temp)): #copy or store temporary array into orginal array/list
        arr[indx+start]=temp[indx]
    

def mergesort(arr,start,end):
    if(start<end):
        mid=int(start+(end-start)/2)
        mergesort(arr,start,mid) #left side
        mergesort(arr,mid+1,end) #right side
        merge(arr,start,mid,end) #perfrom the merge function
  
  #as it is divided by 2 for that time complexity :n/(2^k)=1  -----2^k because divided by two until it get one element
                                                # n=2^k
                                                #log(n)=log(2^k)
                                                #log(n)=klog(2)
                                                #k=log(n)/log(2)
                                                #k=log2^n



arr=list(map(int,input().split(',')))
mergesort(arr,0,len(arr)-1)
print(arr)