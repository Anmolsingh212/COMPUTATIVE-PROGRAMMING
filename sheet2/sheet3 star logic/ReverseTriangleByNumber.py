# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3
# 1 2
# 1
a=int(input("enter the no : "))
for i in range(a,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()