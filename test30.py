n=int(input("Enter the number of rows :"))

for i in range(n,0,-1):
    for j in range(i):
        print(j+1,end=" ")
    print()

# Output :
# 1 2 3 4 5 6 7 8 9 10 
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1