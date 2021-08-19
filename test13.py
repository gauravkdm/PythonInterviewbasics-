import collections

list1= [1,2,3,4,5,6]
list2= [6,5,4,3,2,1]
list3= [9,3,4,5,6,1]

if collections.Counter(list1) == collections.Counter(list2):
    print("Yes they are same ")
else:
    print("No, They are not same ")
if collections.Counter(list1) == collections.Counter(list3):
    print("Yes they are same ")
else:
    print("No, They are not same ")

    # Output :
    # Yes they are same 
    # No, They are not same 