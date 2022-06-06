def stringsum(s):
    sum=0
    for x in s:
        if(x.isdigit()):
            sum=sum+int(x)
    return sum
x=input("Enter string")
print(stringsum(x))