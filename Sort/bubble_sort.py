#! /usr/bin/python3

"""
stable
space: O(1)
time:   O(n^2) [worse, avg]
compare times:      (n-1) + (n-2) + ... + 1 = n(n-1)/2
"""

import  unittest

def bubble_sort(lst):
    for passnum in range(len(lst)-1, 0, -1):
        for i in range(passnum):
            # print(lst)
            if lst[i] > lst[i+1]:
                tmp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = tmp

class Test(unittest.TestCase):
    testLst = []

    def test_null_sort(self):
        testLst = []
        bubble_sort(testLst)
        self.assertEqual(testLst, [])
    def test_one_sort(self):
        testLst = [1]
        bubble_sort(testLst)
        self.assertEqual(testLst, [1])
    def test_sort(self):
        testLst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        bubble_sort(testLst)
        self.assertEqual(
            testLst,
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        testLst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        bubble_sort(testLst)
        self.assertEqual(
            testLst,
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        testLst = [1, 9, 2, 8, 3, 7, 4, 6, 5]
        bubble_sort(testLst)
        self.assertEqual(
            testLst,
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )

if __name__ == '__main__':
    unittest.main()
