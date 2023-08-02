import array as ary
A=ary.array("i",[1,2,3,4,5,6])
l=0
h=len(A)-1
flag=0
key=int(input("Enter the key to be searched: "))
while(l<=h):
    mid=int((l+h)/2)
    if(A[mid]==key):
        print(mid)
        flag=1
        break
    elif(key<A[mid]):
        h=mid-1
    elif(key>A[mid]):
        l=mid+1
if(flag==0):
    print("Key not found")