A=[10,15,7,5,13]
def solve(A):
    t=0;
    m=max(A)
    for i in A: 
        if i!=m:
            t=t+m-i
    return t
print (solve(A))