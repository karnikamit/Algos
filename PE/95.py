__author__ = 'CYBORG'
# Amicable chains


def sum_proper_divisors(n):
    i, j = 1, 0
    while i < n:
        if n % i == 0:
            j += i
        i += 1
    return j


def find_am_pairs(till):
    c, no = 0, 0
    for i in range(till):
        s = sum_proper_divisors(i)
        s1 = sum_proper_divisors(s)
        if s1 == i:
            r = i - s
            if r > c:
                print(i)
                c = r
                no = i
    return no

print(find_am_pairs(100000))
