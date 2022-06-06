def swapx(a,b):
    a=a^b
    b=a^b
    a=a^b
    return a,b
x=int(input("Enter 1st no"))
y=int(input("Enter 2nd no"))
print(swapx(x,y))
