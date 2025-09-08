# *___*
# *___*
# *___*
# *___*
a=int(input("enter the no :"))
for i in range(1,a):
    for j in range(1,a+1):
        if j==1 or j==a:
            print("*",end="")
        else:
            print("_",end="")
    print()