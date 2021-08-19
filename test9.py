list1=['Hello','my','name','is ','gaurav']
print("Actual list :",list1)
n=input("Enter the name you want to insert in the list :")
ind= int(input("Enter the index you want to insert the element :"))
list1.insert(ind, n)
print(list1)

# Output :
# Actual list : ['Hello', 'my', 'name', 'is ', 'gaurav']
# Enter the name you want to insert in the list :kadam
# Enter the index you want to insert the element :5
# ['Hello', 'my', 'name', 'is ', 'gaurav', 'kadam']
