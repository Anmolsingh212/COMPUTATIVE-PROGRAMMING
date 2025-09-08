# * * * * * * * * * * 
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *
a=int(input("enter the no : "))
for i in range(a,0,-1):
    for j in range(i):
        print("*",end=" ")
    for k in range(0,a-i):
        print(" ",end=" ")
    for k in range(0,a-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()