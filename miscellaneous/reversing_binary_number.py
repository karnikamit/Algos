__author__ = 'karnikamit'


def rev_binary_num(n):
    n_rev = n
    s = n.bit_length()
    while n:
        n_rev <<= 1
        n_rev |= n & 1
        s -= 1
        n >>= 1
    n_rev <<= s
    return n_rev


print rev_binary_num(9)