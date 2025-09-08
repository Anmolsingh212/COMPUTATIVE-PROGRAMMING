# ____* 
# ___* *
# __* * *
# _* * * *
# * * * * *
a=int(input("enter the no :"))
for i in range(1,a+1):
    for j in range(a-i):
        print("_",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()