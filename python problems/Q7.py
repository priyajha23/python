def maxfreq(a):

    n=max(max(a),len(a))

    f =[0 for y in range(n)]
    for x in a:
        f[x] = f[x] + 1
    m=max(f)
    return f.index(m)

l = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    x = int(input())

    l.append(x)
print(maxfreq(l))