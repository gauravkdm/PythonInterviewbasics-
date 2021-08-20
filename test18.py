# How to concatenate two strings in Python ?
# 1. Using + operator 

Firstname = "Gaurav"
Lastname = " Kadam"
Name = Firstname + Lastname
print(Name)

# Output :
# Gaurav Kadam

# 2. Using join () method 

joinName = "".join([Firstname,Lastname])
print(joinName)

# Output :
# Gaurav Kadam

# 3. Using % Operator 

print("%s%s" %(Firstname,Lastname))

# Output :
# Gaurav Kadam

# Using Format Function 

print("{} {}".format(Firstname,Lastname)) 

# Output :

# Gaurav Kadam