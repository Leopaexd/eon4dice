from unittest import TestCase
from src.eon4dice import eon4dice


class Test(TestCase):
    def test_roll(self):
        test_strings = [
            '5T6+2',
            '1T6',
            '1t100',
            '2T6+0'
        ]
        for test in test_strings:
            assert(eon4dice.roll(test) > 0)
