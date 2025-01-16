a=[2,4,3,9,8,7]
def print_sub(a):
    b=[]
    if(a[0]%2==0):
        prev='even'
        b.append(a[0])
    if(a[0]%2!=0):
        prev='odd'
    for i in range(1,len(a)):
        if (prev=='even' and a[i]%2!=0):
            b.append(a[i])
            prev='odd'
        if (prev=='even' and a[i]%2==0):
            continue
        if (prev=='odd' and a[i]%2==0):
            b.append(a[i])
            prev='even'
        if (prev=='odd' and a[i]%2!=0):
            continue
    return b
print (print_sub(a))