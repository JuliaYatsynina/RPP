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
