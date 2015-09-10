__author__ = 'karnikamit'
import math
"""
This solution is for this particular equation only.
"""


result = 0
e = "1*5/6*(7+8)"
flag = True
res = 1


def eval_bracaket(string, index):
    new_string = string[index:]
    ret = 0
    stack = []
    for num in new_string:
        if num == '(':
            stack.append(num)
        elif num == ')':
            stack.pop()
        if num == '+':
            i = new_string.index(num)
            ret = (int(new_string[i-1]) + int(new_string[i+1]))
        if num == '*':
            i = new_string.index(num)
            ret = (int(new_string[i-1]) * int(new_string[i+1]))
        if num == '-':
            i = new_string.index(num)
            ret = (int(new_string[i-1]) - int(new_string[i+1]))
        if num == '/':
            i = new_string.index(num)
            ret = (int(new_string[i-1]) / int(new_string[i+1]))

    if not stack:   # confirming bracket balance
        return ret


# conditioning according to precedence
print 'original', e
if '(' in e:
    o = e.find('(')
    new1 = e[:o]
    new1 += str(eval_bracaket(e, o))
    e = new1
print 'e after bracket', e
if '/' in e:
    o = e.find('/')
    res = int(math.ceil(float(int(e[o-1])) / float(int(e[o+1]))))
    new1 = e[:o-1]+str(res)+e[o+2:]
    e = new1
print 'e after division', e
if '*' in e:
    o = e.find('*')
    res1 = int(e[o-1])*int(e[o+1])
    new1 = str(res1) + e[o+2:]
    e = new1
print 'e after multiplication', e