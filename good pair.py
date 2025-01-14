def good_pair(a,b):
    i=0
    j=0
    for i in range (5):
        for j in range (5):
            if a[i]!=a[j] and a[i]+a[j]==b:
               print(a[i],a[j])
    return 
a=[0,2,4,6,8]
b=6
g=good_pair(a,b)
print(g)
