# Stack Has total  4 Operations  :
# 1. Push 
# 2. Pop 
# 3.isEmpty ()
# 4.top or peek


# 1.Implement Stack Using List :

# To push elements in Stack we use append function in List Method :
stack =[]
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)

# [10, 20, 30, 40]

# To pop element from the stack we use pop () function :
stack.pop()
print(stack)

# [10, 20, 30]
# To check whether Stack is Empty or not :

print(len(stack)==0)
# False 

# To access the last element of the stack :

print(stack[-1])
# 30


# Actual Implementation of Stack using list :

stack=[]

def pushelement():
    n=int(input("Enter the elements to push in stack :"))
    stack.append(n)
    print(stack)
def popelement():
    if not stack:
        print("Stack is Empty ! Insert Elements in the Stack :")
    else:
        stack.pop()
        print(stack)

while True:
    print("Select the operation : 1. Push 2. Pop 3. Quit ")
    choice = int(input("Enter your choice :"))
    if choice == 1 :
        pushelement()
    elif choice == 2:
        popelement()
    elif choice == 3:
        break 
    else :
        print("You have entered invalid Choice :")