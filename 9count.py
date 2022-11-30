#aim: To display minimum no of notes
#author : aakash
#date: 8/11/22

amt=int(input("Enter the amount="))
count=0
if amt>=2000:
    q=amt/2000
    print("2000-->",q)
    count=count+q
    amt=amt//2000
elif amt>=500:
    q=amt/500
    print("500-->",q)
    count=count+q
    amt=amt//500
elif amt>=200:
    q=amt/200
    print("200-->",q)
    count=count+q
    amt=amt//200
elif amt>=100:
    q=amt/100
    count=count+q
    amt=amt//100
print("Total no, of notes",count)
