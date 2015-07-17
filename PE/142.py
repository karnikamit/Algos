#ints x>y>z, x+y, x-y, x+z, x-z, y+z, y-z are perfect squares
from math import sqrt
a,b,c,d,e,f = 0,0,0,0,0,0
def num_type(n):
    m = sqrt(n)
    if m.is_integer():
        return True
    #else:
        #print (n, 'n is not an int')
        
i = list(range(1, 100))
for j in range(len(i)-2):
    global a,b,c,d,e,f
    x = i[j+2]
    y = i[j+1]
    z = i[j]
    a = x+y
    #print (a, 'a')
    if num_type(a):
        b = x-y
    if num_type(b):
        c = x+z
    if num_type(c):
        d = x-z
    if num_type(d):
        e = y+z
    if num_type(e):
        f = y-z
    if num_type(f):
        print (x,y,z, 'are the nos')


# num_type(3.3)
