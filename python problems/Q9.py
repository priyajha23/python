def stringsort(s):
    l=sorted(s)
    a=""
    for x in l:
        print(a+x,end="")
    return ""
x=input("Enter string")

print(stringsort(x))