#! /usr/bin/python3

"""
stable
space: O(n)
time:   O(nlogn) [avg]
compare times:      ((nlogn)/2) ~ (nlogn  -n + 1)
assignment times: 2nlogn
"""

import unittest
from collections import deque

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        merged, left, right = deque(), deque(left), deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())
        merged.extend(right if right else left)
        return list(merged)

    middle = int(len(lst) // 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)

class Test(unittest.TestCase):
    def test_null_sort(self):
        self.assertEqual(merge_sort([]), [])
    def test_one_sort(self):
        self.assertEqual(merge_sort([1]), [1])
    def test_sort(self):
        self.assertEqual(
            merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(
            merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(
            merge_sort([1, 9, 2, 8, 3, 7, 4, 6, 5]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )

if __name__ == '__main__':
    unittest.main()
