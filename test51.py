for row in range(7):
    for col in range(5):
        if (col==0 or (col==4 and row>3 and row <6 )or (col==3 and row>3 and row<5) or row==0 or row==6):
            print("*",end="")
        else :
            print(end=" ")
    print()


# Output :
# *****
# *    
# *
# *
# *  **
# *   *
# *****