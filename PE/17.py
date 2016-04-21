# -*- coding: utf-8 -*-
__author__ = "karnikamit"


def number_leter(n):
    first = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
             8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
             14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
             19: 'nineteen', 0: ''}

    second = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
              6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety', 1: 'one'}
    n_str = str(n)
    if len(n_str) == 4:
        name = 'onethousand'
    elif len(n_str) == 3:
        if int(n_str[1:]) > 19:
            name = '%shundredand%s%s' % (first[int(n_str[0])], second[int(n_str[1])], first[int(n_str[2])])
        else:
            name = '%shundredand%s' % (first[int(n_str[0])], first[int(n_str[1:])])
    elif len(str(n)) == 2 and n > 19:
        name = '%s%s' % (second[int(n_str[0])], first[int(n_str[1])])
    else:
        name = '%s' % first[n]
    return len(name)


def num_letter_count():
    letters = 0
    for i in xrange(1, 1001):
        letters += number_leter(i)
    return letters

if __name__ == '__main__':
    # print number_leter(5)
    print num_letter_count()
    # print number_leter(342),len('onehundredandfifteen'), len('onehundredandfifteen')
