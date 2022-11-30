#aim: with arg with return, to find the biggest of 2 numbers
#author : aakash
#date: 8/11/22

def big(a,b):
    if a>b:
        return a
    else:
        return b
x=int(input("enter the first number "))
y=int(input("enter the second number "))
re=big(x,y)
print(re, "is biggest")

