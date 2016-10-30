# -*- coding: utf-8 -*-
__author__ = 'karnikamit'


class Account(object):
    def __init__(self, name, age, account_number, balance=0, dead=False):
        self.name = name
        self.age = age
        self.acc_number = account_number
        self.balance = balance
        self.dead = dead

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
