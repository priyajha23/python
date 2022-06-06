def calculator(a, b, c):
    if (b == '+'):
        print(a + c)
    elif (b == '-'):
        print(a - c)
    elif (b == '*'):
        print(a * c)
    elif (b == '/'):
        print(a / c)
    else:
        print("Invalid")
    return ""


x = int(input("Enter first no"))
z = int(input("Enter second no"))
y = input("Enter the operation you want to perform")
print(calculator(x, y, z))
