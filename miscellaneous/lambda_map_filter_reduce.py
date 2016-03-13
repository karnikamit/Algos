# -*- coding: utf-8 -*-
__author__ = "karnikamit"

'''
The lambda operator or lambda function is a way to create small anonymous functions,
i.e. functions without a name
Throw away functions, i.e these functions are needed where they are created

lambda syntax:
    lambda argument_list: expression
'''
#  Ex:

f = lambda x, y: x+y
print f(1, 2)


'''
map function
r = map(func, seq)
The first argument func is the name of a function and
the second a sequence (e.g. a list) seq.
map() applies the function func to all the elements of the sequence seq.

    It returns a new list with the elements changed by func
                    ------
'''


def fahrenheit(T):
    return (float(9)/5)*T + 32
temp = range(30, 35)

print map(fahrenheit, temp)

#   USING lambda
print map(lambda t: (float(9)/5)*t + 32, temp)

# map() can be applied to more than one list. The lists have to have the same length.
#                                                                        ------------
# map() will apply its lambda function to the elements of the argument lists,
# i.e. it first applies to the elements with the 0th index,
# then to the elements with the 1st index until the n-th index is reached

a = b = range(10)
print map(lambda x, y: x+y, a, b)


'''
filter function
The function filter(function, list) offers an elegant way to filter out all the elements of a list
The function filter(f,l) needs a function f as its first argument. f returns a Boolean value[True/False]
    This function will be applied to every element of the list:
    Only if f returns True will the element of the list be included in the result list

                      ----
'''

# get even numbers
nos = range(100)
print filter(lambda x: x % 2 == 0, nos)

# get odd numbers
print filter(lambda x: x % 2, nos)


'''
Reducing a list
---------------
The function reduce(func, seq) continually applies the function func() to the sequence seq.
It returns a single value
             ------------
At first the first two elements of seq will be applied to func,
i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]

In the next step func will be applied on the previous result and the third element of the list,
                              ------------------------------         -------------
i.e. func(func(s1, s2),s3)
The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]

Continue like this until just one element is left and return this element as the result of reduce()
                         ------------------------

'''