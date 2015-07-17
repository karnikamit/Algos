__author__ = 'karnikamit'


class PrimeRemainders:
    def __init__(self):
        self.prime = None
        self.prime_nos = [i for i in xrange(2, 10000) if self.is_prime(i)]

    def is_prime(self, n):
        return all([(n % j) for j in xrange(2, int(n**0.5)+1)]) and n > 1

    def get_prime_sq_remainders(self, n):
        self.prime = self.prime_nos[n-1]
        numarator = ((self.prime-1)**n + (self.prime+1)**n)
        denominator = (self.prime**2)
        print numarator, denominator
        return numarator/denominator

    def main(self):
        for i in xrange(2, 10000):
            r = self.get_prime_sq_remainders(i)
            if r >= 1000000000:
                return self.prime
        return "NOT Found!"

p = PrimeRemainders()
print p.main()
