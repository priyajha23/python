
def duplicate(a):
    b=[0 for x in range(0,99)]
    for i in a:
        b[i-1] = b[i-1]+1
    return b.index(2)+1

c = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    x = int(input())

    c.append(x)

print(duplicate(c))
