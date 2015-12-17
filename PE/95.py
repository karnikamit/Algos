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


# for i in xrange(100, 104):
#     globals()
#     ori_num = i
#     print find_am_chain(ori_num)

# def find_longest_am_chain(till):
#     longest_am_list = []
#     for i in xrange(till):
#
#         temp = find_am_chain(i, i, am_list)
#         if temp:
#             if len(temp) > len(longest_am_list):
#                 longest_am_list = temp
#     return longest_am_list
#
# print find_longest_am_chain(100)