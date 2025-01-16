A=[10,20,30,40,50,60]
B=2
def rotation(A,B):
    j=len(A)-1
    for i in range(0,(len(A))//2):
        temp=A[j]
        A[j]=A[i]
        A[i]=temp
        j-=1
    print(A)
    j=B-1
    for i in range(0,(B)//2):
        temp=A[j]
        A[j]=A[i]
        A[i]=temp
        j-=1
    print(A)
    j=len(A)-1
    i=B
    while(i<j):
        temp=A[j]
        A[j]=A[i]
        A[i]=temp
        i+=1
        j-=1
    return A
print(rotation(A,B))