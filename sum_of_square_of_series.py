#aim:Arithmetic series 4
#author:aakash
#date: 21/11/22

sum=0
a=1
N=int(input("enter n value : "))
x=int(input("enter x value : "))
for i in range(1,N+1):
    sum=sum+x**a
    a=a+1
print("sum of the series : ", sum)
