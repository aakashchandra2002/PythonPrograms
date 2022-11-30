#aim:Arithmetic series 3
#author:aakash
#date: 21/11/22

sum=0
a=9
N=int(input("enter n value : "))
for i in range(1,N+1):
    sum=sum+a
    a=a+4
print("sum of the series : ", sum)
