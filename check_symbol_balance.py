__author__ = 'karnikamit'
'''
check symbol balance using string iterations
'''


def check_symbol_balance(data):
    p = "()"
    c = "{}"
    sq = "[]"
    count_p, count_c, count_sq = 0, 0, 0
    for item in data:
        if item == p[0]:
            count_p += 1
        elif item == c[0]:
            count_c += 1
        elif item == sq[0]:
            count_sq += 1
        elif item == p[1]:
            count_p -= 1
        elif item == c[1]:
            count_c -= 1
        elif item == sq[1]:
            count_sq -= 1
    if count_p == 0 and count_c == 0 and count_sq == 0:
        return True
    return False

# ip = "([]{()({})})"
# print check_symbol_balance(ip)

"""
check symbol balance using dict and stack
"""

from stack import Stack


def chk_synm_bal(data):
    s = Stack()
    check = {"{": "}", "[": "]", "(": ")"}
    balanced = False
    for item in data:
        if item in check.keys():
            s.push(item)
        if item in check.values():
            try:
                symbol = s.pop()
                if item == check[symbol]:
                    balanced = True
                else:
                    balanced = False
            except IndexError:
                balanced = False
    return balanced

ip = "([]{()({})})"
print chk_synm_bal(ip)
