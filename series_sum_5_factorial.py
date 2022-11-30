#aim:Arithmetic series 5
#author:aakash
#date: 21/11/22

import math as m
sum=0
a=9
N=int(input("enter n value : "))
x=int(input("enter x value : "))
for i in range(1,N+1):
    sum=sum+m.factorial(a)/x
    a=a+1
print("sum of the series : ", sum)
