import unittest
from fleshkincaid import Fleshkincaid


class TestFleshkincaid(unittest.TestCase):

    def test_class_defined(self):
        flshkncd = Fleshkincaid('Hi')
        self.assertTrue(isinstance(flshkncd, Fleshkincaid))


if __name__ == "__main__":
    unittest.main()
