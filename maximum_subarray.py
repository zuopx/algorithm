""""""
import unittest


def maximum_subarray(array: list[int, float]) -> list[int, float]:
    len_ = len(array)
    if len_ <= 1:
        return [0, len_]

    povit = len_ // 2
    a, b = maximum_subarray(array[:povit])
    c, d = maximum_subarray(array[povit+1:])
    c, d = c + povit, d + povit

    e, s = povit, 0
    for i in range(0, povit):
        if sum(array[i:povit]) > s:
            e = i

    f, s = povit+1, 0
    for i in range(povit, len_):
        if sum(array[povit+1:i]) > s:
            f = i

    g, h = e, f
    if sum(array[a:b]) > sum(array[g:h]):
        g, h = a, b
    if sum(array[c:d]) > sum(array[g:h]):
        g, h = c, d

    return g, h


class MaximumSubarrayTest(unittest.TestCase):
    def test_maximum_subarray(self):
        in_ = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        out = maximum_subarray(in_)
        self.assertTupleEqual(out, (7, 11))
        print(in_[out[0]:out[1]])


def main():
    print("hello, world")
    unittest.main()


if __name__ == "__main__":
    main()
