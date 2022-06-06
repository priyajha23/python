def palin(s):
    for i in range(0, int(len(s) / 2)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True
x=input("Enter string")
print(palin(x))


