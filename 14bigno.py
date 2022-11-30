#aim: program to find biggest of 3 numbers
#author: aakash
#date: 8/11/22

a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)
