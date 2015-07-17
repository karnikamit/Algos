a = range(90, 101)
b = range(90, 101)
mds = 0
for num in a:
    mds1 = []
    for num1 in b:
        ds = num ** num1
        x = sum(map(int,str(ds)))
        mds1.append(x)
    if max(mds1) > mds:
        mds = max(mds1)
print(mds)
