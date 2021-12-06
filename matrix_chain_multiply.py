"""矩阵链乘"""
import sys
from typing import Tuple
import unittest

from dynamic_programming import extended_rod_cutting


def mcm_top_down(shapes: list) -> int:
    n = len(shapes) - 1
    return _mcm_top_down(shapes, 1, n)


def _mcm_top_down(shapes: list, head: int, tail: int) -> int:
    if head == tail:
        return 0

    if tail - head == 1:
        return shapes[head - 1] * shapes[head] * shapes[tail]

    q = sys.maxsize
    for i in range(head, tail):
        r = _mcm_top_down(shapes, head, i) + _mcm_top_down(shapes, i + 1, tail)
        r += shapes[head - 1] * shapes[i] * shapes[tail]
        q = min(q, r)

    return q


def mcm_bottom_up(shapes: list) -> int:
    n = len(shapes) - 1
    m = {}
    for d in range(1, n):
        for head in range(1, n - d + 1):
            tail = head + d

            q = sys.maxsize
            for i in range(head, tail):
                r = m.get((head, i), 0) + m.get((i + 1, tail), 0)
                r += shapes[head - 1] * shapes[i] * shapes[tail]
                q = min(q, r)

            m[(head, tail)] = q

    return m[(1, n)]


def extended_mcm_bottom_up(shapes: list) -> Tuple[int, str]:
    n = len(shapes) - 1
    m, s = {}, {}
    for d in range(1, n):
        for head in range(1, n - d + 1):
            tail = head + d

            q = sys.maxsize
            for i in range(head, tail):
                r = m.get((head, i), 0) + m.get((i + 1, tail), 0)
                r += shapes[head - 1] * shapes[i] * shapes[tail]
                if r < q:
                    q = r
                    s[(head, tail)] = i

            m[(head, tail)] = q

    return m[(1, n)], _print_optimal_parens(s, 1, n)


def _print_optimal_parens(s: dict, head: int, tail: int) -> str:
    if head == tail:
        return str(head)
    else:
        return "(" + _print_optimal_parens(s, head, s[(head, tail)]) +\
            _print_optimal_parens(s, s[(head, tail)] + 1, tail) + ")"


class TestMatrixChainMultiply(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.shapes = [30, 35, 15, 5, 10, 20, 25]
        self.optimal = 15125

    def test_top_down(self):
        self.assertEqual(self.optimal, mcm_top_down(self.shapes))

    def test_bottom_up(self):
        self.assertEqual(self.optimal, mcm_bottom_up(self.shapes))

    def test_extended_mcm(self):
        print(extended_mcm_bottom_up(self.shapes))


def main():
    unittest.main()
    print("hello, world")


if __name__ == "__main__":
    main()
