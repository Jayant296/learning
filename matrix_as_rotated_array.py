A=[1,2,3,4,5]
B=[2,3,4]
def rotation(A,B):
    mat=[]
    k=0
    while(k<len(B)):
        temp=[]
        i=B[k]
        while(i<len(A)):
            temp.append(A[i])
            i+=1
        i=0
        while(i<B[k]):
            temp.append(A[i])
            i+=1
        mat.append(temp)
        k+=1
    return mat
print(rotation(A,B))