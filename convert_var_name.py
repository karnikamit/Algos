# -*- coding: utf-8 -*-
__author__ = "karnikamit"
import re


def replace1(match):
    return match.group(1)+'_'+match.group(2).lower()


def convert_to_snake_case(var):
    return re.sub(r'(.)([A-Z])', replace1, var)


def replace2(match):
    return match.group(2).upper()


def cov_back_to_camel_case(var_name):
    s2 = re.sub('([_])(.)', replace2, var_name)
    return s2

if __name__ == '__main__':
    name = 'camelCaseCasesYo'
    snake_case = convert_to_snake_case(name)
    print 'original: %s' % name
    print 'converted: %s' % snake_case
    print 'conv back: %s' % cov_back_to_camel_case(snake_case)
