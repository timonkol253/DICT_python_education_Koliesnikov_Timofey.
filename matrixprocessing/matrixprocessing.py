import sys

def read_matrix():
    """
    Зчитує матрицю з введених користувачем даних.

    Користувач вводить розмір матриці (рядки та стовпці), а потім самі елементи матриці.

    Повертає:
        list[list[float]]: матриця, введена користувачем, або None, якщо введені дані некоректні.
    """
    rows, cols = map(int, input("Enter size of matrix: > ").split())
    print("Enter matrix:")
    matrix = []
    for _ in range(rows):
        row = list(map(float, input("> ").split()))
        if len(row) != cols:
            print("ERROR: Invalid number of elements in row.")
            return None
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    """
    Виводить матрицю на екран у зручному форматі.

    Аргументи:
        matrix (list[list[float]]): матриця для виведення.
    """
    for row in matrix:
        print(' '.join(str(round(num, 2)).replace('.0 ', ' ').replace('.0', '') for num in row))

def add_matrices():
    """
    Виконує додавання двох матриць.

    Користувач вводить дві матриці однакового розміру. Функція виводить їх суму.
    Якщо розміри матриць не співпадають, виводить повідомлення про помилку.
    """
    print("Enter size of first matrix: > ", end='')
    rows1, cols1 = map(int, input().split())
    print("Enter first matrix:")
    matrix1 = []
    for _ in range(rows1):
        row = list(map(float, input("> ").split()))
        matrix1.append(row)

    print("Enter size of second matrix: > ", end='')
    rows2, cols2 = map(int, input().split())
    print("Enter second matrix:")
    matrix2 = []
    for _ in range(rows2):
        row = list(map(float, input("> ").split()))
        matrix2.append(row)

    if rows1 != rows2 or cols1 != cols2:
        print("ERROR")
        return

    result = []
    for i in range(rows1):
        result_row = []
        for j in range(cols1):
            result_row.append(matrix1[i][j] + matrix2[i][j])
        result.append(result_row)

    print("The result is:")
    print_matrix(result)

def multiply_by_constant():
    """
    Множить матрицю на константу.

    Користувач вводить матрицю та константу. Функція виводить результат множення.
    """
    matrix = read_matrix()
    if matrix is None:
        return
    constant = float(input("Enter constant: > "))

    result = []
    for row in matrix:
        result_row = [element * constant for element in row]
        result.append(result_row)

    print("The result is:")
    print_matrix(result)

def multiply_matrices():
    """
    Виконує множення двох матриць.

    Користувач вводить дві матриці. Функція перевіряє, чи можна їх перемножити
    (кількість стовпців першої має дорівнювати кількості рядків другої).
    Виводить результат множення або повідомлення про помилку.
    """
    print("Enter size of first matrix: > ", end='')
    rows1, cols1 = map(int, input().split())
    print("Enter first matrix:")
    matrix1 = []
    for _ in range(rows1):
        row = list(map(float, input("> ").split()))
        matrix1.append(row)

    print("Enter size of second matrix: > ", end='')
    rows2, cols2 = map(int, input().split())
    print("Enter second matrix:")
    matrix2 = []
    for _ in range(rows2):
        row = list(map(float, input("> ").split()))
        matrix2.append(row)

    if cols1 != rows2:
        print("The operation cannot be performed.")
        return

    result = []
    for i in range(rows1):
        result_row = []
        for j in range(cols2):
            sum_val = 0
            for k in range(cols1):
                sum_val += matrix1[i][k] * matrix2[k][j]
            result_row.append(sum_val)
        result.append(result_row)

    print("The result is:")
    print_matrix(result)

def transpose_matrix():
    """
    Виконує транспонування матриці згідно з обраним користувачем методом.

    Користувач обирає тип транспонування:
    1. По головній діагоналі
    2. По побічній діагоналі
    3. По вертикальній лінії
    4. По горизонтальній лінії

    Виводить результат транспонування.
    """
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    choice = input("Your choice: > ")

    matrix = read_matrix()
    if matrix is None:
        return

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    if choice == '1':  # Main diagonal
        result = [[matrix[j][i] for j in range(cols)] for i in range(rows)]
    elif choice == '2':  # Side diagonal
        result = [[matrix[cols - 1 - j][rows - 1 - i] for j in range(cols)] for i in range(rows)]
    elif choice == '3':  # Vertical line
        result = [row[::-1] for row in matrix]
    elif choice == '4':  # Horizontal line
        result = [matrix[rows - 1 - i] for i in range(rows)]
    else:
        print("Invalid choice")
        return

    print("The result is:")
    print_matrix(result)

def get_minor(matrix, i, j):
    """
    Обчислює мінор матриці для елемента (i, j).

    Аргументи:
        matrix (list[list[float]]): вихідна матриця
        i (int): індекс рядка
        j (int): індекс стовпця

    Повертає:
        list[list[float]]: мінор матриці
    """
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def calculate_determinant(matrix):
    """
    Обчислює визначник матриці рекурсивним методом (методом розкладання по рядку).

    Аргументи:
        matrix (list[list[float]]): квадратна матриця

    Повертає:
        float: значення визначника
    """
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for c in range(len(matrix)):
        minor = get_minor(matrix, 0, c)
        determinant += ((-1) ** c) * matrix[0][c] * calculate_determinant(minor)

    return determinant


def show_determinant():
    """
    Обчислює та виводить визначник матриці, введеної користувачем.

    Якщо матриця не квадратна, виводить повідомлення про помилку.
    """
    matrix = read_matrix()
    if matrix is None:
        return

    if len(matrix) != len(matrix[0]):
        print("The operation cannot be performed.")
        return

    det = calculate_determinant(matrix)
    print("The result is:")
    print(det)


def inverse_matrix():
    """
    Обчислює та виводить обернену матрицю.

    Користувач вводить квадратну матрицю. Функція перевіряє, чи існує обернена матриця
    (визначник не дорівнює нулю). Виводить результат або повідомлення про помилку.
    """
    matrix = read_matrix()
    if matrix is None:
        return

    if len(matrix) != len(matrix[0]):
        print("The operation cannot be performed.")
        return

    det = calculate_determinant(matrix)
    if det == 0:
        print("This matrix doesn't have an inverse.")
        return

    n = len(matrix)
    cofactors = []

    for r in range(n):
        cofactor_row = []
        for c in range(n):
            minor = get_minor(matrix, r, c)
            cofactor_row.append(((-1) ** (r + c)) * calculate_determinant(minor))
        cofactors.append(cofactor_row)

    adjugate = [[cofactors[j][i] for j in range(n)] for i in range(n)]
    inverse = [[adjugate[i][j] / det for j in range(n)] for i in range(n)]

    print("The result is:")
    print_matrix(inverse)

def main():
    """
    Головна функція, яка реалізує меню для роботи з матрицями.

    Користувач може вибрати одну з операцій:
    1. Додавання матриць
    2. Множення матриці на константу
    3. Множення матриць
    4. Транспонування матриці
    5. Обчислення визначника
    6. Знаходження оберненої матриці
    0. Вихід з програми
    """
    while True:
        print("\n1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: > ")

        if choice == '1':
            add_matrices()
        elif choice == '2':
            multiply_by_constant()
        elif choice == '3':
            multiply_matrices()
        elif choice == '4':
            transpose_matrix()
        elif choice == '5':
            show_determinant()
        elif choice == '6':
            inverse_matrix()
        elif choice == '0':
            sys.exit()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()