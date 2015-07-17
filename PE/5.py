n = 1
for i in range(1, 21):
    if n % i > 0:
        for j in range(1, 21):
            if (n*j) % i == 0:
                n *= j
                break
print (n)

'''
def gcd(a, b):
    if (b == 0): return a
    else: return gcd(b, a%b)

def lcm(a, b):
    return abs(a*b) / gcd(a, b)

def euler5(n):
    if (n == 1): return 1
    else: return lcm(n, euler5(n-1))

print (euler5(20))

def delbart(t,n):
    if n > 0:
        if not (t%n):
            if delbart(t, n-1):
                return True
            else:
                return False
        else:
            return False
    else:
        return True

i = 20
while not delbart(i,20):
    i +=20

print (i)
'''
