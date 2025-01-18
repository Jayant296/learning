A=[9,9,9]
def add_one(A):
    num=''
    for i in A:
        st=str(i)
        num+=st
    num=int(num)
    num+=1
    print(num)
    n=num
    A.clear()
    while(n>0):
        rem=n%10
        A.append(rem)
        n=n/10
    print(A)
    i=0
    j=len(A)-1
    while(i<j):
        temp=A[j]
        A[j]=A[i]
        A[i]=temp
        i+=1
        j-=1
    return A
print(add_one(A))