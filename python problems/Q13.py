def oddcount(a):
    for x in a:
        if(a.count(x)%2==1):
            return x
l = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    x = int(input())

    l.append(x)
print(oddcount(l))