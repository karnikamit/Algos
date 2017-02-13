# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from datetime import datetime


class Person(object):
    def __init__(self, first_name, last_name, dob):
        self.f_name = first_name
        self.l_name = last_name
        self.dob = dob

    @property
    def get_name(self):
        return "{0}.{1}".format(self.f_name, self.l_name)

    @property
    def get_dob(self):
        mbr_dob = datetime.strptime(self.dob, '%M/%d/%Y')
        return mbr_dob

    @get_dob.setter
    def get_dob(self, value):
        raise NotImplementedError


class Account(Person):

    def __init__(self, first_name, last_name, dob, acc_no, balance=0):
        super(self.__class__, self).__init__(first_name, last_name, dob)
        self.balance = balance
        self.acc_no = acc_no

    @property
    def deposit(self):
        return self.balance

    @deposit.setter
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        msg = 'Not Sufficient funds'
        if self.balance > amount:
            self.balance -= amount
            msg = 'Withdrawing rs: {0}/-'.format(amount)
        return msg

    @property
    def get_acc_no(self):
        return self.acc_no

    @get_acc_no.setter
    def get_acc_no(self, value):
        raise NotImplementedError

    def __str__(self):
        return 'Name: {0} DOB: {3}\nAcconun Number: {1}\n' \
               'Balance:{2} (subject to clearing)'.format(self.get_name, self.acc_no, self.deposit, self.get_dob)


class AnotherParent(object):

    def __init__(self, idn, roll_no):
        object.__setattr__(self, 'idn', idn)
        object.__setattr__(self, 'roll_no', roll_no)


class Parent(object):

    def __init__(self, idn):
        object.__setattr__(self, 'idn', idn)

    def __str__(self):
        return 'Parent is called'

    # Making this object immutable
    def __setattr__(self, key, value):
        raise TypeError(' {} object does not support item assignment'.format(self.__class__))

class Child(AnotherParent, Parent):
    pass
