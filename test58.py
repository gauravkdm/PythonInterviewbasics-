for row in range(7):
    for col in range(7):
        if (col==0 or col ==6 or (row==col and row>0 and row<6)):
            print("*",end="")
        else:
            print(end=" ")
    print()

# Output :
# *     *
# **    *
# * *   *
# *  *  *
# *   * *
# *    **
# *     *