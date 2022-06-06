def prime(a,b):
    p = [0 for y in range(a,b+1)]
    for x in range(a,b+1):
        if (x > 1):
            for i in range(2, int(x**0.5) + 1):
                if (x % i == 0):
                    p[x-a] = 1
                    break
        else:
            p[x-a]=1
    pri=[]
    for z in range(len(p)):
        if(p[z]==0):
            pri.append(z+a)
    return pri
r1=int(input("Enter the beginning of range"))
r2=int(input("Enter the end of range"))
print(prime(r1,r2))


