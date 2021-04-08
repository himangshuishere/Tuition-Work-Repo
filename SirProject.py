"""
Q1. 
i)
*
* *
* * *
"""
for i in range(4):
    for j in range(i):
        print("*", end = " ")
    print()

"""
Q1.
ii)
    *
  * *
* * *
"""
for i in range(4):
    for j in range(3,0,-1):
        if i>=j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()