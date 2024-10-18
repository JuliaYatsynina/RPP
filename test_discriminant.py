import pytest
from discriminant import calculate_discriminant


def test_calculate_discriminant():
    # Положительные тесты
    assert calculate_discriminant(1, -3, 2) == 1, "Test case 1 failed"
    assert calculate_discriminant(1, 0, -4) == 16, "Test case 2 failed"
    assert calculate_discriminant(1, 2, 1) == 0, "Test case 3 failed"

    # Негативные тесты
    assert calculate_discriminant(1, 1, 1) == -3, "Test case 4 failed"
    assert calculate_discriminant(1, 0, 1) == -4, "Test case 5 failed"


if __name__ == "__main__":
    pytest.main()
