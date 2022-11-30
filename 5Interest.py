#aim:program to calculate Interest I value
#author: aakash
#date:8/11/22

#interest I=PTR/100

P=int(input("enter the principle amt: "))
T=int(input("enter the time: "))
R=int(input("enter the rate of interest: "))
I=P*T*R/100
print("Interest calculated = ",I)
