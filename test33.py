n= int(input("Enter the number of rows :"))
ascivalue=65

for i in range (1,n+1):
    for j in range(1, i+1):
        alphabet= chr(ascivalue)
        print(alphabet ,end=" ")
        ascivalue = ascivalue + 1
    print()

# Output :
# Enter the number of rows :7
# A 
# B C
# D E F
# G H I J
# K L M N O
# P Q R S T U
# V W X Y Z [ \