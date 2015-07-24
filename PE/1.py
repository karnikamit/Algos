
print sum(i for i in range(1000) if (i % 3 == 0) or (i % 5 == 0))  # One Liner

'''
while n < 334:
    while i < 200:
        o = 5*i
        print(o)
    p = 3*n
    n = n + 1
    print(p)
'''
'''
while i < 200:
    o = 5*i
    i = i+1
    print(o)
print("the ans- ",p+o)
 '''   

def get_multiples(limit):
    flag = True
    n = 0
    mult = []
    while flag:
        n += 1
        n_3 = 3*n
        n_5 = 5*n
        if n_3 < limit:
            mult.append(n_3)
        if n_5 < limit:
            mult.append(n_5)
        if n_3 >= limit:
            flag = False
    print mult
    return mult

# print sum(get_multiples(1000))