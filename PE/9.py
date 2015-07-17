__author__ = 'CYBORG'


def euler9():
    for c in range(2, 1000):
        for a in range(1, c):
            # Ensure a + b + c == 1000.  Since a is counting up, the first
            # answer we find should have a <= b.
            b = 1000 - c - a

            # Ensure Pythagorean triple
            if a**2 + b**2 == c**2:
                print("a = %d, b = %d, c = %d.  abc = %d" % (a, b, c, a * b * c))
                return

euler9()
