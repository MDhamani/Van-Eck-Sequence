#####################################
############# MDhamani ##############
#####################################
import matplotlib.pyplot as pyt
t = int(input("enter van eck values to generate:- "))
t = t - 2
a, b = 0, 0
l = []
l.append(a)
l.append(b)
while t != 0:
    c = 0
    k = 0
    l.reverse()
    b = l[0]
    for x in l[1:]:
        c = c + 1
        if b == x:
            l.reverse()
            l.append(c)
            k = 1
            break
    if k == 0:
        l.reverse()
        l.append(0)
    t = t - 1
print(l)
pyt.plot(l)
pyt.show()
