#aim:functions
#author : aakash
#date:2/11/22


def display():
    a=int(input("enter any integer"))
    b=int(input("enter any integer"))
    if a>b:
        print("{}>{}".format(a,b))
    else:
        print("{}<{}".format(a,b))
        
display()
