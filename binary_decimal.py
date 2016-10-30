# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
'''
Convert the given binary number to decimal.
'''


class NumberConverter(object):
    """
    Class to convert the given number to decimal from binary or vice-versa.
    """
    def __init__(self, number):
        self.number = []
        if isinstance(number, int):
            self.number = map(int, list(str(number)))

    def __del__(self):
        return 'NumberConverter instance is destroyed'

    def binay_to_decimal(self):
        """
        Method to convert to decimal
        :return: Decimal equivalent number.
        """
        decimal = [v * (2**i) for i, v in enumerate(self.number[::-1])]
        return sum(decimal)

    def decimal_binary(self):
        """
        Method to convert binary number to decimal.
        :return: Binary equivalent number.
        """
        self.number = int(''.join(map(str, (self.number))))
        if self.number < 2:
            return str(self.number)
        return self._get_binary(self.number)

    def _get_binary(self, n):
        if n < 2:
            return str(n)
        return self._get_binary(n//2) + str(n % 2)


if __name__ == '__main__':
    n = NumberConverter(5)
    print n.decimal_binary()
