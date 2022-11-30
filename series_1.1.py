#aim:Arithmetic series 2
#author:aakash
#date: 21/11/22

sum=0
a=1
N=int(input("enter n value : "))
for i in range(1,N+1):
    sum=sum+a
    a=a+1
print("sum of the series : ", sum)
