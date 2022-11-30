#aim:program to calculate S value
#author: aakash
#date:8/11/22

u=int(input("Enter the initial velocity="))
t=int(input("Enter the time="))
a=int(input("Enter acceleration value="))
s=u*t+a*t*t*0.5
print("Distance (S)= ",s)
