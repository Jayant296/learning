A=5
def matrix(A):
    mat=[[0]*A for _ in range (A)]
    r,c=0,0
    num=1
    while A>=1:
        for i in range(A-1):#loop is iterating 4 times at first time.
            mat[r][c]=num
            c+=1
            num+=1
        for i in range(A-1):
            mat[r][c]=num
            r+=1
            num+=1
        for i in range(A-1):
            mat[r][c]=num
            c-=1
            num+=1
        for i in range(A-1):
            mat[r][c]=num
            r-=1
            num+=1
        A-=2
        r+=1
        c+=1
        if A==1:
            mat[r][c]=num
    for row in mat:
        print(row)
        print()
print(matrix(A))
