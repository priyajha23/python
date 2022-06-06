def countype(a):
    digit=0
    char=0
    special=0
    for x in a:
        if(x.isdigit()):
            digit=digit+1
        elif(x.isalpha()):
            char=char+1
        else:
            special=special+1
    print("[digit, char, special]=",end="")
    print([digit,char,special])
    return ""


s=input("Enter string")
print(countype(s))

