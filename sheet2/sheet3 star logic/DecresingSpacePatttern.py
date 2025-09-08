# *_____*
# *____*
# *___*
# *__*
# *_*
a=int(input("enter the no :"))
for i in range(a,0,-1):
    print("*",end="")
    for j in range(i,0,-1):
        print("_",end="")
    print("*")