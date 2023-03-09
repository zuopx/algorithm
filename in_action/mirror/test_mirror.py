from unittest import TestCase
from main import Mirror


class TestMirror(TestCase):
    def setUp(self):
        self.mirror = Mirror(5, 5, 5)

    def test_print(self):
        s = str(self.mirror)
        print(s)


if __name__ == "__main__":
    import unittest
    unittest.main()
    pass
