#aim: with arg with return, to find the biggest of 3 numbers with 2 arguments
#author : aakash
#date: 8/11/22

def big(a,b):
    if a>b:
        return a
    else:
        return b
x=int(input("enter the first number "))
y=int(input("enter the second number "))
z=int(input("enter the second number "))
p=big(x,y)
q=big(p,z)
print(q, "is biggest")

