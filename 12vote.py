#aim: to display voting eligibility
#author: aakash
#date: 8/11/22

age= int(input())
if age>=18:
    print("You can vote")
elif age>0 and age<=17:
    print("You are a child")
else:
    print("You cant Vote")
