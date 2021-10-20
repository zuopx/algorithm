""""""
import unittest
import numpy as np


def matrix_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    assert A.shape == B.shape
    len_ = len(A)

    if len_ == 1:
        return A * B

    mid = len_ // 2
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]
    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    S1 = B12 - B22
    S2 = A11 + A12
    S3 = A21 + A22
    S4 = B21 - B11
    S5 = A11 + A22
    S6 = B11 + B22
    S7 = A12 - A22
    S8 = B21 + B22
    S9 = A11 - A21
    S10 = B11 + B12

    P1 = matrix_multiply(A11, S1)
    P2 = matrix_multiply(B22, S2)
    P3 = matrix_multiply(B11, S3)
    P4 = matrix_multiply(A22, S4)
    P5 = matrix_multiply(S5, S6)
    P6 = matrix_multiply(S7, S8)
    P7 = matrix_multiply(S9, S10)

    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7

    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return C


class MatrixMultiplyTest(unittest.TestCase):
    def test_matrix_multiply(self):
        N = 2
        A = np.random.randint(0, 100, size=(N, N))
        B = np.random.randint(0, 100, size=(N, N))

        C = matrix_multiply(A, B)

        self.assertTrue(np.array_equal(np.dot(A, B), C))


def main():
    unittest.main()
    print("hello, world")


if __name__ == "__main__":
    main()
