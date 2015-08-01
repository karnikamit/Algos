__author__ = 'karnikamit'


# print 'Right shift', 5 >> 4
# print 'Left shift', 5 << 1
# print 'AND', 8 & 5
# print 'OR', 9 | 4
# print 'XOR', 12 ^ 42
# print 'NOT', ~88

# checking whether Kth bit is set ot not

n = 00000010
K = 4
num = n & (1 << K-1)
if "{0:b}".format(num)[0] == '1':
    print 'Kth bit is set.'
else:
    print 'Not set'

# Setting Kth bit
n = 00000000
K = 4
set_num = n | (1 << K-1)
print "{0:b}".format(set_num)

# Clearing Kth bit
n = 00000010
K = 4
num = n & ~(1 << K-1)
print "{0:b}".format(num)