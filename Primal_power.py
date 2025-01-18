A=[1,3,4,5,6,7,89,79,4,55,78,97]
def primal_pow(A):
    count=0
    for j in range(0,len(A)):
        if A[j]>1:
            check_prime=True
            i=2
            while i*i<=A[j]:
                if A[j]%i==0:
                    check_prime=False
                i+=1
            if check_prime==True:
                count+=1
    return count
print(primal_pow(A))
                 
