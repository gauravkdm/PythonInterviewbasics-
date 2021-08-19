list1=[5,3,4,5,7,9]
list2=[9,5,3,4,7,5]

set1= set(list1)
set2= set(list2)
print(set1,set2)
if set1 == set2 :
    print("Yes they are equal ")
else :
    print( "No , They are not equal ")

    # Output :
    # {3, 4, 5, 7, 9} {3, 4, 5, 7, 9}
    # Yes they are equal