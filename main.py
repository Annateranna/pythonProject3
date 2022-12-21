'''
import reverse_2_times
import unittest


class TestReverse(unittest.TestCase):
    def test_a_bigger_than_y(self):
        self.assertEqual(reverse_2_times.reverse_2_times("9 2 5 6 9"), "1 5 4 3 2 9 8 7 6")

    def test_a_smaller_than_y(self):
        self.assertEqual(reverse_2_times.reverse_2_times("9 3 6 5 8"), "1 2 6 5 8 7 3 4 9")


if __name__ == '__main__':
    unittest.main()
'''
import hurracane

if __name__ == '__main__':
    hurracane
