# steps for calculator 


# 1. write addition function
# 2. write subtraction function
# 3. write multiplicaton function
# 4. write division function
# 5. take input from the user 
# 6. based on the input perform 1,2,3,4 or 5 function 
# 7. store the result into a variable.
# 8. print the variable.


# a = int(input("Provide input number 1 :"))
# b = int(input("Provide input number 2 :"))

# add = (a+b)
# print("addition of a and b is =", add) 

# sub = (a-b)
# print("subtraction of a and b is =", sub)

# mul = (a*b)
# print("multiplication of a and b is =", mul)

# div = (a/b)
# print("division of a and b is =", div)

# remainder = (a%b)
# print("division of a and b is =", remainder)

print("\nWhich operation do you want to perform. Select from the list below. \n1. Addition.\n2. Subtraction.\n3. Multiplication.\n4. Division.\n5. Remainder.")

x = int(input("Enter your decision :"))

if x == 1:
    a = int(input("Provide input number 1 :"))
    b = int(input("Provide input number 2 :"))
    add = (a+b)
    print("addition of a and b is =", add) 

if x == 2:
    a = int(input("Provide input number 1 :"))
    b = int(input("Provide input number 2 :"))
    sub = (a-b)
    print("subtraction of a and b is =", sub) 

if x == 3:
    a = int(input("Provide input number 1 :"))
    b = int(input("Provide input number 2 :"))
    mul = (a*b)
    print("multiplication of a and b is =", mul) 

if x == 4:
    a = int(input("Provide input number 1 :"))
    b = int(input("Provide input number 2 :"))
    div = (a/b)
    print("division of a and b is =", div) 

if x == 5:
    a = int(input("Provide input number 1 :"))
    b = int(input("Provide input number 2 :"))
    remainder = (a%b)
    print("remainder of a and b is =", remainder) 
