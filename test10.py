list1=['Hello','my','name','is ','gaurav']
print("Actual list :",list1)
list1.extend(['nothing','something'])
print(list1)
list1.extend(('ok','gotit'))
print(list1)
list1.extend(("nosometing is missing"))
print(list1)

# Output :
# Actual list : ['Hello', 'my', 'name', 'is ', 'gaurav']
# ['Hello', 'my', 'name', 'is ', 'gaurav', 'nothing', 'something']
# ['Hello', 'my', 'name', 'is ', 'gaurav', 'nothing', 'something', 'ok', 'gotit']
# ['Hello', 'my', 'name', 'is ', 'gaurav', 'nothing', 'something', 'ok', 'gotit', 'n', 'o', 's', 'o', 'm', 'e', 't', 'i', 'n', 'g', ' ', 'i', 's', ' ', 'm', 'i', 's', 's', 'i', 'n', 'g']