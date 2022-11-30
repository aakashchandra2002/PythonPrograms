#aim:functions
#author : aakash
#date:2/11/22


def display():
    P=int(input("enter the principle amount"))
    T=int(input("enter the time"))
    R=int(input("enter the rate of interest"))
    I=(P*T*R)/100
    print("{}+{}+{}/100={}".format(P,T,R,I))
display()
