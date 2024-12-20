def print_grid(grid):
    """
    Етап 1: Виведення ігрового поля.
    Виводить ігрове поле 3x3 з рамками.

    Args:
        grid (list): Двовимірний список, що представляє поле гри.

    Returns:
        None
    """
    print("---------")
    for row in grid:
        print(f"| {' '.join(row)} |")
    print("---------")


def create_grid_from_input(user_input):
    """
    Етап 2: Створення сітки.
    Створює ігрове поле 3x3 із введеного рядка символів.

    Args:
        user_input (str): Рядок із 9 символів ("X", "O" або "_").

    Returns:
        list: Двовимірний список, що представляє ігрове поле.
    """
    return [list(user_input[i:i + 3]) for i in range(0, 9, 3)]


def check_winner(grid):
    """
    Етап 3: Аналіз стану гри.
    Перевіряє стан гри для визначення переможця чи іншого результату.

    Args:
        grid (list): Двовимірний список, що представляє поле гри.

    Returns:
        str: Результат гри ("X wins", "O wins", "Draw", "Game not finished", "Impossible").
    """
    lines = grid + [list(col) for col in zip(*grid)] + [
        [grid[0][0], grid[1][1], grid[2][2]],
        [grid[0][2], grid[1][1], grid[2][0]]
    ]
    x_count = sum(row.count("X") for row in grid)
    o_count = sum(row.count("O") for row in grid)
    x_wins = ["X", "X", "X"] in lines
    o_wins = ["O", "O", "O"] in lines

    if x_wins and o_wins or abs(x_count - o_count) > 1:
        return "Impossible"
    if x_wins:
        return "X wins"
    if o_wins:
        return "O wins"
    if "_" not in sum(grid, []):
        return "Draw"
    return "Game not finished"


def is_valid_move(grid, x, y):
    """
    Етап 4: Перевірка ходу.
    Перевіряє, чи є хід користувача допустимим.

    Args:
        grid (list): Двовимірний список, що представляє поле гри.
        x (int): Рядок, куди хоче зробити хід гравець (1-3).
        y (int): Стовпець, куди хоче зробити хід гравець (1-3).

    Returns:
        bool: True, якщо хід допустимий, інакше False.
    """
    if not (1 <= x <= 3 and 1 <= y <= 3):
        print("Coordinates should be from 1 to 3!")
        return False
    if grid[x - 1][y - 1] != "_":
        print("This cell is occupied! Choose another one!")
        return False
    return True


def make_move(grid, x, y, player):
    """
    Етап 4: Зміна стану поля.
    Робить хід гравця на полі.

    Args:
        grid (list): Двовимірний список, що представляє поле гри.
        x (int): Рядок, куди робиться хід (1-3).
        y (int): Стовпець, куди робиться хід (1-3).
        player (str): Символ гравця ("X" або "O").

    Returns:
        None
    """
    grid[x - 1][y - 1] = player


def play_game():
    """
    Етап 5: Повна гра.
    Основна функція гри "Хрестики-нулики". Забезпечує ігровий цикл між двома гравцями.

    Під час гри програма перевіряє коректність введення, змінює ігрове поле та визначає результат.

    Returns:
        None
    """
    grid = [["_"] * 3 for _ in range(3)]
    print_grid(grid)
    current_player = "X"

    while True:
        while True:
            user_input = input(f"Player {current_player}, enter the coordinates: ").split()
            if len(user_input) == 2 and user_input[0].isdigit() and user_input[1].isdigit():
                x, y = map(int, user_input)
                if is_valid_move(grid, x, y):
                    make_move(grid, x, y, current_player)
                    break
            else:
                print("You should enter two numbers!")

        print_grid(grid)
        result = check_winner(grid)
        if result != "Game not finished":
            print(result)
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()