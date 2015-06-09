__author__ = 'karnikamit'


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.gcd = 0

    def show(self):
        return str(self.num)+'/'+str(self.den)

    def show_lowest(self):
        n, d = self.num, self.den
        while self.den:
            self.num, self.den = self.den, self.num % self.den
        self.gcd = self.num
        return str(n/self.gcd)+'/'+str(d/self.gcd)

    def show_div(self):
        pass

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __div__(self, other):
        new_num = self.num*other.den
        new_den = self.den*other.num
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num*other.num
        new_den = self.den*other.den
        return Fraction(new_num, new_den)


fr = Fraction(3, 2)
fr1 = Fraction(1, 4)
fr3 = fr + fr1
fr4 = fr * fr1
fr5 = fr / fr1
print fr3.show_lowest()
print fr4.show()
print fr5.show_lowest()