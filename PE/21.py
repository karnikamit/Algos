import time


def amicable(n):

    a = 0
    for i in range(1,n):
        if n % i == 0:
            a += i
    b = 0
    for j in range(1, a):
        if a % j == 0:
            b += j
    return a+b

start = time.time()
print(amicable(10000), "Runtime", time.time()-start, "seconds")
