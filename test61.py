for row in range(8):
    for col in range(5):
        if ( col==0 and row!=0 and row!=6 and row!=7) or (col==4 and row!=0 and row!=6) or (row==0 and col!=0 and col!=4) or (row==6 and col!=4 and col!=0) or (col==1 and row>4 and row<6):
            print("*",end="")
        else:
            print(end=" ")
    print()

    # Output:
#  *** 
# *   *
# *   *
# *   *
# *   *
# **  *
#  ***
#     *