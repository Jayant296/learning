A=[10,2,3,4,6,9]
def multiply(A):
    for i in range(0,len(A)):
        if i==0:
            prev=A[i]
            A[i]*=A[i+1]
        elif i==len(A)-1:
            A[i]*=prev
        else:
            temp=A[i]
            A[i]=prev*A[i+1]
            prev=temp
    return A
print(multiply(A))