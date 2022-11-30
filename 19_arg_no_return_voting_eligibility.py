#aim: with arg no return, to find vote eligibility
#author : aakash
#date: 8/11/22

def vote(age):
    if age>=18:
        print("You can VOTE")
    elif age>5 and age<=17:
        print("You are CHILD")
    else:
        print("You can not VOTE")
a=int(input("enter your age "))
vote(a)
