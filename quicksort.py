

def partition(arr,start,end):
    pivot=arr[end]
    index=start-1
    for j in range(start,end):
       if(arr[j]<=pivot):
          index+=1
          temp=arr[j]
          arr[j]=arr[index]
          arr[index]=temp

    temp1=arr[end]
    arr[end]=arr[index+1]
    arr[index+1]=temp1
    return index+1
    
def quicksort(arr,start,end):
    if(start<end):
       pivot_index=partition(arr,start,end)
       quicksort(arr,start,pivot_index-1)
       quicksort(arr,pivot_index+1,end)

#quick sort :
arr=list(map(int,input().split(',')))
quicksort(arr,0,len(arr)-1)
print (arr)


         
         
