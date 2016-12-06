#! /usr/bin/python3

"""
stable
space: O(1)
time:   O(n^2) [worst, avg]
"""

import unittest

def selection_sort(lst):
    for fillslot in range(len(lst)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if lst[location] > lst[positionOfMax]:
                positionOfMax = location

        tmp = lst[fillslot]
        lst[fillslot] = lst[positionOfMax]
        lst[positionOfMax] = tmp

class Test(unittest.TestCase):
    testLst = []
    def test_null_sort(self):
        testLst = []
        selection_sort(testLst)
        self.assertEqual(testLst, [])
    def test_one_sort(self):
        testLst = [1]
        selection_sort(testLst)
        self.assertEqual(testLst, [1])
    def test_sort(self):
        testLst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        selection_sort(testLst)
        self.assertEqual(
            testLst,
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        testLst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        selection_sort(testLst)
        self.assertEqual(
            testLst,
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        testLst = [1, 9, 2, 8, 3, 7, 4, 6, 5]
        selection_sort(testLst)
        self.assertEqual(
            testLst,
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )

if __name__ == '__main__':
    unittest.main()
