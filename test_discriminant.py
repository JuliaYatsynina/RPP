import unittest
from discriminant import calculate_discriminant, main
from unittest.mock import patch


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

    @patch('builtins.input', side_effect=[1, -3, 2])
    @patch('builtins.print')
    def test_main_positive_discriminant(self, mock_print):
        main()
        mock_print.assert_any_call("Дискриминант: 1")
        mock_print.assert_any_call("Два различных вещественных корня.")

    @patch('builtins.input', side_effect=[1, 2, 1])
    @patch('builtins.print')
    def test_main_zero_discriminant(self, mock_print):
        main()
        mock_print.assert_any_call("Дискриминант: 0")
        mock_print.assert_any_call("Один вещественный корень.")

    @patch('builtins.input', side_effect=[1, 1, 1])
    @patch('builtins.print')
    def test_main_negative_discriminant(self, mock_print):
        main()
        mock_print.assert_any_call("Дискриминант: -3")
        mock_print.assert_any_call("Нет вещественных корней.")


if __name__ == "__main__":
    unittest.main()
