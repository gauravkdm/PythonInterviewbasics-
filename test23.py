# Printing Simple-half  Pyramid  Downward :
n= int(input("Enter the number of rows :"))

for i in range (n,0,-1):
    for j in range(0,i):
        print("*", end=" ")
    print()

    # Output :
    # * * * * * 
    # * * * * 
    # * * * 
    # * * 
    # *