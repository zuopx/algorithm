"""最长公共子串"""
import unittest


def lcs_top_down(X: str, Y: str) -> str:
    """自上而下，递归解法，定位子问题"""
    if not X or not Y:
        return ""

    if X[-1] == Y[-1]:
        Z = lcs_top_down(X[:-1], Y[:-1]) + X[-1]
    else:
        Z1 = lcs_top_down(X[:-1], Y)
        Z2 = lcs_top_down(X, Y[:-1])
        Z = Z1 if len(Z1) >= len(Z2) else Z2

    return Z


def lcs_bottom_up(X: str, Y: str) -> str:
    """自下而上，先解决子问题，空间换时间"""
    x, y = len(X), len(Y)
    m = {}

    for i in range(x + 1):
        for j in range(y + 1):
            if not i or not j:
                m[(i, j)] = ""
                continue

            if X[i - 1] == Y[j - 1]:
                m[(i, j)] = m[(i - 1, j - 1)] + X[i - 1]
            else:
                Z1 = m[(i - 1, j)]
                Z2 = m[(i, j - 1)]
                m[(i, j)] = Z1 if len(Z1) >= len(Z2) else Z2

    return m[(x, y)]


class TestLCS(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.X = "ABCBDAB"
        self.Y = "BDCABA"
        self.Z = "BCBA"

    def test_top_down(self):
        self.assertEqual(self.Z, lcs_top_down(self.X, self.Y))

    def test_bottom_up(self):
        self.assertEqual(self.Z, lcs_bottom_up(self.X, self.Y))


def main():
    unittest.main()
    print("hello, world!")


if __name__ == "__main__":
    main()
