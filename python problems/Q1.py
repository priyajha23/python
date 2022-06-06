def my_sort(a,b):
    if(b=='asc'):
        return sorted(a)
    elif(b=='desc'):
        return sorted(a,reverse=True)
    elif(b=='none'):
        return a


l = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    x = int(input())

    l.append(x)
o=input("Enter the order you want it in")


print(my_sort(l,o))
