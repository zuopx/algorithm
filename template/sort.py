"""排序"""
import random
import unittest


def heapsort(array: list[int, float]) -> None:
    build_max_heap(array)
    len_ = len(array)
    for i in range(len_, 0, -1):
        array[0], array[i - 1] = array[i - 1], array[0]
        max_heapify(array, 1, i - 1)


def build_max_heap(array: list[int, float]) -> None:
    len_ = len(array)
    for i in range(len_ // 2, 0, -1):
        max_heapify(array, i, len_)


def max_heapify(array: list[int, float], i: int, len_: int) -> None:
    left, right = _left(i), _right(i)
    largest = i
    if left <= len_ and array[left - 1] > array[largest - 1]:
        largest = left
    if right <= len_ and array[right - 1] > array[largest - 1]:
        largest = right

    if largest != i:
        array[largest - 1], array[i - 1] = array[i - 1], array[largest - 1]
        max_heapify(array, largest, len_)


def _parent(i: int) -> int:
    return i >> 1


def _left(i: int) -> int:
    return i << 1


def _right(i: int) -> int:
    return (i << 1) + 1


class SortTest(unittest.TestCase):
    def setUp(self):
        N = 100
        self.in_ = list(range(N))
        random.shuffle(self.in_)

    def test_heapsort(self):
        heapsort(self.in_)
        self.assertListEqual(sorted(self.in_), self.in_)

    def test_build_max_heap(self):
        build_max_heap(self.in_)
        for i in range(1, len(self.in_) + 1):
            left, right = _left(i), _right(i)
            if left <= len(self.in_):
                assert self.in_[i - 1] >= self.in_[left - 1]
            if right <= len(self.in_):
                assert self.in_[i - 1] >= self.in_[right - 1]


def main():
    unittest.main()
    print("hello, world")


if __name__ == "__main__":
    main()
