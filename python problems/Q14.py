def gcd(a,b):
    if (b == 0):
        return a
    return gcd(b, a%b)

x=int(input("Enter 1st no"))
y=int(input("Enter 2nd no"))

print(gcd(x,y)



