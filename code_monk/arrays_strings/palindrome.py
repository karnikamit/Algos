# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
cases = int(raw_input())
for _ in xrange(cases):
    ip_string = raw_input()
    if ip_string == ip_string[::-1]:
        print 'YES {}'.format('EVEN' if len(ip_string) % 2 == 0 else 'ODD')
    else:
        print 'NO'
