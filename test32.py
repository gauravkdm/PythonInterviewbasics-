n= int(input("Enter the number of rows :"))
ascivalue= int(input("Enter the ASCII Value to Print Pattern :"))
if (ascivalue>= 65 or ascivalue<= 122):
    for i in range (1,n+1):
        for j in range(1, i+1):
            alphabet= chr(ascivalue)
            print(alphabet ,end=" ")
        print()
else:
    print("Enter the valid Character :")


# Output :
# Enter the number of rows :10
# Enter the ASCII Value to Print Pattern :67
# C 
# C C 
# C C C 
# C C C C 
# C C C C C 
# C C C C C C 
# C C C C C C C 
# C C C C C C C C 
# C C C C C C C C C 
# C C C C C C C C C C