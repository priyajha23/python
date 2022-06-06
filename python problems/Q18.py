def eff(a):
    V=a.count("NORTH")-a.count("SOUTH")
    H=a.count("EAST")-a.count("WEST")
    o=""
    if(V>0):
        o=o+str(v)+" "+"NORTH"
    elif(V<0):
        o=o+str(abs(V))+" "+"SOUTH"
    if(H>0):
        o = o + str(H) +" "+ "EAST"
    elif(H<0):
        o = o + str(abs(H))+" " + "WEST"
    return o
l = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    x = input()

    l.append(x)

print(eff(l))