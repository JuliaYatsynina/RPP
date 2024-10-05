def calculate_discriminant(a, b, c):
    """
    Вычисляет дискриминант для квадратного уравнения ax^2 + bx + c = 0.
    """
    return b ** 2 - 4 * a * c


def main():
    print("Введите коэффициенты квадратного уравнения ax^2 + bx + c = 0:")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    discriminant = calculate_discriminant(a, b, c)
    print(f"Дискриминант: {discriminant}")

    if discriminant > 0:
        print("Два различных вещественных корня.")
    elif discriminant == 0:
        print("Один вещественный корень.")
    else:
        print("Нет вещественных корней.")


if __name__ == "__main__":
    main()


def test_calculate_discriminant():
    # Положительные тесты
    assert calculate_discriminant(1, -3, 2) == 1, "Test case 1 failed"
    assert calculate_discriminant(1, 0, -4) == 16, "Test case 2 failed"
    assert calculate_discriminant(1, 2, 1) == 0, "Test case 3 failed"

    # Негативные тесты
    assert calculate_discriminant(1, 1, 1) == -3, "Test case 4 failed"
    assert calculate_discriminant(1, 0, 1) == -4, "Test case 5 failed"

    print("Все тесты пройдены успешно!")


if __name__ == "__main__":
    test_calculate_discriminant()
