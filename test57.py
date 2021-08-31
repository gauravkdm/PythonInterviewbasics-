
for row in range(7):
    for col in range(5):
        if (col==0 or col==4 or (row==col and row<3 and col<3)or (col==3 and row==1)):
            print("*",end="")
        else:
            print(end=" ")
    print()

# # Output :

# *   *
# ** **
# * * *
# *   *
# *   *
# *   *
# *   *


for row in range(7):
    for col in range(7):
        if (col==0 or col==6) or  (col==row and col <4 and row < 4) or (row==2 and col==4  ) or (row==1 and col==5):
            print("*",end="")
        else:
            print(end=" ")
    print()

# Output :
# *     *
# **   **
# * * * *
# *  *  *
# *     *
# *     *
# *     *