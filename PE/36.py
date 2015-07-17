#Double - Base palindromes
import time
start = time.clock()
palindromes = 0
for n in range(1, 1000000):
    number = n
    num = list(map(int, str(n)))
    num1 = num[::-1]
    base = []
    b = n%2
    base.append(b)
    while n > 1:
        n //=  2    #Floor division by the base
        a = n%2     #Getting the remainder
        base.append(a)
        
    v = base[::-1]
    #print v
    if base == v and num == num1:
        palindromes += number
print (palindromes,'sum of all palindromes')
end = time.clock()
print ('Runtime:', end-start, 'sec')
