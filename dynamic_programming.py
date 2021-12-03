""""""
import unittest
import sys


def rod_cutting_top_down(prices: list, n: int) -> int:
    """自上而下"""
    if n == 0:
        return 0

    q = -sys.maxsize - 1
    for i in range(n):
        q = max(q, prices[i] + rod_cutting_top_down(prices, n - i - 1))

    return q


Q = {}


def rod_cutting_use_memory(prices: list, n: int) -> int:
    """使用缓存"""
    if n == 0:
        return 0

    global Q
    if n in Q:
        return Q[n]

    q = -sys.maxsize - 1
    for i in range(n):
        q = max(q, prices[i] + rod_cutting_top_down(prices, n - i - 1))

    Q[n] = q
    return q


def rod_cutting_bottom_up(prices: list, n: int) -> int:
    """由下而上

    先解决小问题，
    当遇到大问题时，它的小问题都已经得到了解决。
    """
    r = {}

    for i in range(n):
        q = -sys.maxsize - 1
        for j in range(i + 1):
            q = max(q, prices[j] + r.get(i - j, 0))

        r[i + 1] = q

    return r[n]


class DynamicProgrammingTest(unittest.TestCase):
    def test_rod_cutting_top_down(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 10

        expected = [1, 5, 8, 10, 13, 17, 18, 22, 25, 30]
        actual = [rod_cutting_top_down(prices, i + 1) for i in range(n)]
        self.assertListEqual(expected, actual)

    def test_rod_cutting_use_memory(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 10

        expected = [1, 5, 8, 10, 13, 17, 18, 22, 25, 30]
        actual = [rod_cutting_use_memory(prices, i + 1) for i in range(n)]
        self.assertListEqual(expected, actual)

    def test_rod_cutting_bottom_up(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 10

        expected = [1, 5, 8, 10, 13, 17, 18, 22, 25, 30]
        actual = [rod_cutting_bottom_up(prices, i + 1) for i in range(n)]
        self.assertListEqual(expected, actual)


def main():
    unittest.main()
    print("hello, world")


if __name__ == "__main__":
    main()
