#aim:no arg no return, to find the sum of distance S in S=ut+0.5at*t
#author : aakash
#date: 8/11/22

def sum():
    u=int(input("enter a value "))
    t=int(input("enter a value "))
    a=int(input("enter a value "))
    s=u*t+0.5*a*t*t
    print("u is {} t is {} a is {} s is {}".format(u,t,a,s))
sum()
