import unittest
import my_function

fun = fun()

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    # Returns True if the string contains 4 a.
    def test_strings_a(self):
        self.assertEqual('a' * 4, 'aaaa')

        # Returns True if the string is in upper case.

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    # Returns TRUE if the string is in uppercase
    # else returns False.
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    # @staticmethod
    # def add(a,b):
    #     return a+b

    @patch fun.add()
    def test_add(self):
        self.assertEqual(self.add(2,3),5)


if __name__ == '__main__':
    unittest.main()