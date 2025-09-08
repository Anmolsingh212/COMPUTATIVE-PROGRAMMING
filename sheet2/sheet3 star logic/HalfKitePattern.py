# * 
# ** 
# *** 
# **** 
# ***** 
# **** 
# *** 
# ** 
# * 

a=int(input("enter the no : "))
for i in range(a):
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(a,0,-1):
    for j in range(i-1):
        print("*", end=" ")
    print()
