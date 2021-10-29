"""Selection Problem

Input: A set A of n (distinct) numbers and an integer i, with 1 <= i <= n.
Output: The element x in A that is larger than exactly i - 1 other elements of A.
"""
from typing import Union
import random
import unittest
import timeit


def selection(array: list[int, float], order: int) -> Union[int, float]:
    in_ = array[:]
    len_ = len(in_)
    if len_ < 140:
        return sorted(in_)[order - 1]

    medians = []
    b, e = 0, 5
    while e <= len_:
        _swap_sort(in_, b, e)
        medians.append(in_[b + 2])
        b, e = e, e + 5

    m = selection(medians, len(medians) // 2)

    i, j = 0, 0
    while j < len_:
        if in_[j] < m:
            in_[i], in_[j] = in_[j], in_[i]
            i += 1
        j += 1

    z = 1
    while in_[z - 1] != m:
        z += 1
    in_[i], in_[z - 1] = in_[z - 1], in_[i]
    z = i + 1

    if z == order:
        return m
    elif z < order:
        return selection(in_[z:], order - z)
    else:
        return selection(in_[:z], order)


def _swap_sort(array: list[int, float], b: int, e: int) -> None:
    for i in range(b + 1, e):
        z = i
        for j in range(i - 1, b - 1, -1):
            if array[z] < array[j]:
                array[z], array[j] = array[j], array[z]
                z = j
            else:
                break


class SelectionTest(unittest.TestCase):
    def setUp(self):
        self.N = 10000
        self.in_ = list(range(self.N))
        random.shuffle(self.in_)

    def test_selection(self):
        for i in random.sample(range(self.N), 100):
            self.assertEqual(i, selection(self.in_, i + 1))

    def test_swap_sort(self):
        _swap_sort(self.in_, 0, self.N)
        self.assertListEqual(sorted(self.in_), self.in_)


def main():
    unittest.main()
    print("hello, world")


if __name__ == "__main__":
    main()
