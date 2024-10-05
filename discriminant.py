def calculate_discriminant(a, b, c):
    """
        a (float): Коэффициент при x^2.
        b (float): Коэффициент при x.
        c (float): Свободный член.
    """
    discriminant = b ** 2 - 4 * a * c
    return discriminant


def main():
    print("Введите коэффициенты квадратного уравнения:")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    discriminant = calculate_discriminant(a, b, c)

    print(f"Дискриминант квадратного уравнения {a}x^2 + {b}x + {c} = 0 равен {discriminant}")

    if discriminant > 0:
        print("Уравнение имеет два различных действительных корня.")
    elif discriminant < 0:
        print("Уравнение имеет два комплексных корня.")
    else:
        print("Уравнение имеет один действительный корень.")


if __name__ == "__main__":
    main()
