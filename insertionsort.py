#insertion sort insert the smaller value in a right position and shift the others
#It also saves its current value and index for insertion
#input :64, 34, 25, 12, 22, 11, 90, 5
l=list(map(int,input().split(',')))
n=len(l)
for i in range(1,n): #it let 1st(64)element is sorted.to compare with others element we will check from index 1(34)than  to last element.
    current_index=i
    current_value=l[i]
    for j in range(i-1,-1,-1):#this check the sorted array if i=3 it will check 2,1,0 index comparison to place value in a right place
        if(l[j]>current_value): # example of this condition:if 
            l[j+1]=l[j]
            current_index=j
        else:
            break
    l[current_index]=current_value
print(l)
            
            