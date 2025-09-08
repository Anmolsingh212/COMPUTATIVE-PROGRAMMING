# * * * * * 
# _* * * *
# __* * *
# ___* *
# ____*
a=int(input("enter the no : "))
for i in range(0,a):
    for j in range(i):
        print("_",end="")
    for k in range(a-i):
        print("*",end=" ")
    print()