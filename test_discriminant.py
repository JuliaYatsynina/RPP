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

    def test_large_numbers(self):
        self.assertEqual(calculate_discriminant(1000, 2000, 1000), 0)
        self.assertEqual(calculate_discriminant(1000, 2000, 500), 2000000)

    def test_small_numbers(self):
        self.assertAlmostEqual(
            calculate_discriminant(0.1, 0.2, 0.1), 0.0, places=7)
        self.assertAlmostEqual(
            calculate_discriminant(0.1, 0.2, 0.05), 0.02, places=7)

    def test_negative_coefficients(self):
        self.assertEqual(calculate_discriminant(-1, -3, -2), 1)
        self.assertEqual(calculate_discriminant(-1, -3, -1), 5)

    def test_zero_coefficients(self):
        self.assertEqual(calculate_discriminant(0, 0, 0), 0)
        self.assertEqual(calculate_discriminant(0, 1, 0), 1)
        self.assertEqual(calculate_discriminant(0, 0, 1), 0)

    def test_mixed_coefficients(self):
        self.assertEqual(calculate_discriminant(1, -1, -1), 5)
        self.assertEqual(calculate_discriminant(-1, 1, 1), 5)

    def test_all_zero_coefficients(self):
        self.assertEqual(calculate_discriminant(0, 0, 0), 0)

    def test_large_negative_coefficients(self):
        self.assertEqual(calculate_discriminant(-1000, -2000, -1000), 0)
        self.assertEqual(calculate_discriminant(-1000, -2000, -500), 2000000)

    def test_large_positive_coefficients(self):
        self.assertEqual(calculate_discriminant(1000000, 2000000, 1000000), 0)
        self.assertEqual(calculate_discriminant(1000000, 2000000, 500000), 2000000000000)

    def test_small_coefficients(self):
        self.assertEqual(calculate_discriminant(0.0001, 0.0002, 0.0001), 0.0)
        self.assertEqual(calculate_discriminant(0.0001, 0.0002, 0.00005), 0.000002)

    def test_coefficients_with_large_difference(self):
        self.assertEqual(calculate_discriminant(1, 10000, 1), 99999600)
        self.assertEqual(calculate_discriminant(1, -10000, 1), 99999600)


if __name__ == "__main__":
    unittest.main()
