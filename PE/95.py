__author__ = 'CYBORG'
# Amicable chains


def sum_proper_divisors(n):
    j = 0
    for i in xrange(1, int(n >> 1)+1):
        if not n % i:
            j += i
    return j


def find_am_chain(num, am_list):
    s = sum_proper_divisors(num)
    am_list.append(s)
    if s == am_list[0]:
        return am_list[:-1]
    elif s < ori_num:
        return []
    return find_am_chain(s, am_list)

num = maximum = 1
for ori_num in xrange(1, 12497):
    am_list = list([ori_num])
    length = len(find_am_chain(ori_num, am_list))
    (num, maximum) = length > maximum and (ori_num, length) or (num, maximum)
print num, maximum
