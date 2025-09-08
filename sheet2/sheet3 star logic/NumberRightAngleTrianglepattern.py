# 1 
# 1 *
# 1 * 3
# 1 * 3 *
# 1 * 3 * 5
a=int(input("enter the no : "))
for i in range(1,a+1):
    for j in range(1,i+1):
        if j%2!=0:
            print(j,end=" ")
        else:
            print("*",end=" ")
    print()