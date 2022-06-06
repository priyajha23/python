def card(a):
    for x in range(len(a)-4):
        print('*',end='')
    for x in a[-4:]:
        print(x,end='')
    return ''

c=input("Enter card no.")
print(card(c))