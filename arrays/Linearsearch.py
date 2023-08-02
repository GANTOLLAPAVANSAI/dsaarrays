import array as ary
A=ary.array("i",[1,2,3,4,5,6])
key=3
flag=0
for i in range(0,len(A)):
    if(A[i]==key):
        print(i)
        flag=1
if(flag==0):
    print("Key is not found")
