"""Priority queue is a heap.

How to design CRUD operation?
"""
import sys
import random
from typing import Union
import unittest


class Item:
    def __init__(self, key: Union[int, float], *args):
        self.key = key
        self.args = args


class MaxPriorityQueue:
    def __init__(self):
        self.data = []

    def insert(self, e: Item) -> None:
        self.data.append(Item(-sys.maxsize - 1))
        self.increase_key(len(self.data), e.key)

    def maximum(self) -> Item:
        return self.data[0]

    def extract_max(self) -> Item:
        len_ = len(self.data)
        self.data[0], self.data[len_ - 1] = self.data[len_ - 1], self.data[0]
        e = self.data.pop()
        self.max_heapify(1)
        return e

    def increase_key(self, i: int, k: Union[int, float]) -> None:
        assert self.data[i - 1].key < k

        self.data[i - 1].key = k
        parent = i >> 1
        while i > 1 and self.data[parent - 1].key < self.data[i - 1].key:
            self.data[parent - 1], self.data[i - 1] = self.data[i - 1], self.data[parent - 1]
            i, parent = parent, parent >> 1

    def max_heapify(self, i: int) -> None:
        len_ = len(self.data)
        left, right = i << 1, (i << 1) + 1
        largest = i
        if left <= len_ and self.data[left - 1].key > self.data[largest - 1].key:
            largest = left
        if right <= len_ and self.data[right - 1].key > self.data[largest - 1].key:
            largest = right

        if largest != i:
            self.data[i - 1], self.data[largest - 1] = self.data[largest - 1], self.data[i - 1]
            self.max_heapify(largest)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        return self.data[i]


class MaxPriorityQueueTest(unittest.TestCase):
    def setUp(self):
        self.in_ = MaxPriorityQueue()
        self.N = 100
        seq = list(range(self.N))
        random.shuffle(seq)
        for k in seq:
            self.in_.insert(Item(k))

    def test_insert(self):
        for i in range(1, len(self.in_) + 1):
            left, right = i << 1, (i << 1) + 1
            if left <= len(self.in_):
                assert self.in_[i - 1].key >= self.in_[left - 1].key
            if right <= len(self.in_):
                assert self.in_[i - 1].key >= self.in_[right - 1].key

    def test_maximum(self):
        self.assertEqual(self.N - 1, self.in_.maximum().key)

    def test_extract_max(self):
        self.assertEqual(self.N - 1, self.in_.extract_max().key)
        self.assertEqual(self.N - 1, len(self.in_))

        for i in range(1, len(self.in_) + 1):
            left, right = i << 1, (i << 1) + 1
            if left <= len(self.in_):
                assert self.in_[i - 1].key >= self.in_[left - 1].key
            if right <= len(self.in_):
                assert self.in_[i - 1].key >= self.in_[right - 1].key

    def test_increase_key(self):
        for i in random.sample(range(self.N), 10):
            self.in_.increase_key(i + 1, self.in_[i].key + random.randint(1, 10))

        for i in range(1, len(self.in_) + 1):
            left, right = i << 1, (i << 1) + 1
            if left <= len(self.in_):
                assert self.in_[i - 1].key >= self.in_[left - 1].key
            if right <= len(self.in_):
                assert self.in_[i - 1].key >= self.in_[right - 1].key


def main():
    unittest.main()
    print("hello, world")


if __name__ == "__main__":
    main()
