a = int(input("enter the size of array: "))
def FizzBuzz(a):
    arr=[]
    for i in range(1,a+1):
        if i%3==0 and i%5!=0:
           arr.append("Fizz")
        elif i%5==0 and i%3!=0:
           arr.append("Buzz")
        elif i%3==0 and i%5==0:
           arr.append("FizzBuzz")
        else:
           arr.append(i)
    return arr
F=FizzBuzz(a)
print(F)