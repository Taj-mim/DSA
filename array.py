#finding min value of an array we can solve it using 

# built-in function min()
# using loops 
#using sorting method


#using built-in function min()
l=[9,20,1,2,10,3,-1]
print("using min function:", min(l))


minval=l[0]
for i in range(len(l)):
    if(l[i]<minval):
        minval=l[i]
print("using loops:", minval)

l.sort()
print("using sorting method:", l[0] )

#same for finding max value of an array 