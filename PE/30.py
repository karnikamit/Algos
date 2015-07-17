import time
start = time.clock()
fp = 0
for i in range(2, 230000):
    b = list(map(int, str(i)))
    a = []
    for j in b:
        a.append(j**5)
    if sum(a) == i:
        fp += i
print ('sum', fp)
print ('Runtime:', time.clock()-start, 'sec')
