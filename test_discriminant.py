import unittest
from discriminant import calculate_discriminant


class TestCalculateDiscriminant(unittest.TestCase):
    def test_positive_discriminant(self):
        self.assertEqual(calculate_discriminant(1, -3, 2), 1)
        self.assertEqual(calculate_discriminant(1, 0, -4), 16)
        self.assertEqual(calculate_discriminant(1000, 2000, 500), 2000000)
        self.assertAlmostEqual(
            calculate_discriminant(0.1, 0.2, 0.05), 0.02, places=7)
        self.assertEqual(calculate_discriminant(-1, -3, -2), 1)
        self.assertEqual(calculate_discriminant(-1, -3, -1), 5)
        self.assertEqual(calculate_discriminant(0, 1, 0), 1)
        self.assertEqual(calculate_discriminant(1, -1, -1), 5)
        self.assertEqual(calculate_discriminant(-1, 1, 1), 5)
        self.assertEqual(calculate_discriminant(-1000, -2000, -500), 2000000)
        self.assertEqual(calculate_discriminant
                         (0.001, 0.002, 0.0005), 0.000002)
        self.assertEqual(calculate_discriminant(0, 3, 0), 9)
        self.assertEqual(calculate_discriminant(0, 6, 7), 36)
        self.assertEqual(calculate_discriminant(1, 5, -4), 41)
        self.assertEqual(calculate_discriminant(7, -3, -7), 205)
        self.assertEqual(calculate_discriminant(6, -1, -4), 97)
        self.assertEqual(calculate_discriminant(5, 6, 1), 16)
        self.assertEqual(calculate_discriminant(0, 2, 0), 4)
        self.assertEqual(calculate_discriminant(0, 1, 7), 1)
        self.assertEqual(calculate_discriminant(5, 6, 0), 36)

    def test_zero_discriminant(self):
        self.assertEqual(calculate_discriminant(1, 2, 1), 0)
        self.assertEqual(calculate_discriminant(1000, 2000, 1000), 0)
        self.assertAlmostEqual(
            calculate_discriminant(0.1, 0.2, 0.1), 0.0, places=7)
        self.assertEqual(calculate_discriminant(0, 0, 0), 0)
        self.assertEqual(calculate_discriminant(0, 0, 1), 0)
        self.assertEqual(calculate_discriminant(-1000, -2000, -1000), 0)
        self.assertEqual(calculate_discriminant(0.001, 0.002, 0.001), 0.0)
        self.assertEqual(calculate_discriminant(0, 0, 3), 0)

    def test_negative_discriminant(self):
        self.assertEqual(calculate_discriminant(1, 1, 1), -3)
        self.assertEqual(calculate_discriminant(1, 0, 1), -4)
        self.assertEqual(calculate_discriminant(1, 2, 3), -8)
        self.assertEqual(calculate_discriminant(77, 3, 7), -2147)
        self.assertEqual(calculate_discriminant(6, 1, 4), -95)
        self.assertEqual(calculate_discriminant(-1, 1, -4), -15)
        self.assertEqual(calculate_discriminant(8, -1, 7), -223)


if __name__ == "__main__":
    unittest.main()
