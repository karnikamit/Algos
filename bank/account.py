# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from baseclasses import Account

# TODO Need to work with DB!

class HDFCBank(Account):
    pass


class ICICIBank(Account):
    pass

h = HDFCBank('Amit', 27, 'HDFC007', 100)
print h.acc_number
