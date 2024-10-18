import unittest
from discriminant import calculate_discriminant


class TestCalculateDiscriminant(unittest.TestCase):
    def test_positive_discriminant(self):
        self.assertEqual(calculate_discriminant(1, -3, 2), 1)
        self.assertEqual(calculate_discriminant(1, 0, -4), 16)

    def test_zero_discriminant(self):
        self.assertEqual(calculate_discriminant(1, 2, 1), 0)

    def test_negative_discriminant(self):
        self.assertEqual(calculate_discriminant(1, 1, 1), -3)
        self.assertEqual(calculate_discriminant(1, 0, 1), -4)


if __name__ == "__main__":
    unittest.main()
