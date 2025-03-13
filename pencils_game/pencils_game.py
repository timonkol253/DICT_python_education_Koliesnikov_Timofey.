import random

def get_pencils():
    """
    Запитує у користувача кількість олівців та перевіряє введені дані.

    Повертає:
        int: Кількість олівців.
    """
    while True:
        pencils = input("How many pencils would you like to use:\n> ")
        if not pencils.isdigit():
            print("The number of pencils should be numeric")
            continue
        pencils = int(pencils)
        if pencils <= 0:
            print("The number of pencils should be positive")
            continue
        return pencils


def get_first_player(name1, name2):
    """
    Запитує у користувача, хто буде першим гравцем.

    Аргументи:
        name1 (str): Ім'я першого гравця.
        name2 (str): Ім'я другого гравця.

    Повертає:
        str: Ім'я першого гравця.
    """
    while True:
        first_player = input(f"Who will be the first ({name1}, {name2}):\n> ")
        if first_player not in (name1, name2):
            print(f"Choose between '{name1}' and '{name2}'")
            continue
        return first_player


def print_pencils(pencils):
    """
    Виводить кількість олівців на столі.

    Аргументи:
        pencils (int): Кількість олівців.
    """
    print("|" * pencils)


def stage1():
    """
    Основна функція для першого етапу.
    Виконує введення кількості олівців та вибір першого гравця.
    """
    name1, name2 = "John", "Jack"
    pencils = get_pencils()
    first_player = get_first_player(name1, name2)
    print_pencils(pencils)
    print(f"{first_player} is going first!")
    return pencils, first_player, name1, name2

def take_pencils(player, pencils):
    """
    Запитує у гравця кількість олівців, яку він хоче взяти.

    Аргументи:
        player (str): Ім'я гравця.
        pencils (int): Кількість олівців на столі.

    Повертає:
        int: Кількість взятих олівців.
    """
    while True:
        try:
            taken = int(input(f"{player}'s turn:\n> "))
            if taken not in (1, 2, 3):
                print("Possible values: '1', '2' or '3'")
                continue
            if taken > pencils:
                print("Too many pencils were taken")
                continue
            return taken
        except ValueError:
            print("Possible values: '1', '2' or '3'")


def stage2(pencils, first_player, name1, name2):
    """
    Основна функція для другого етапу.
    Реалізує гру з чергуванням гравців.
    """
    current_player = first_player
    while pencils > 0:
        print_pencils(pencils)
        taken = take_pencils(current_player, pencils)
        pencils -= taken
        if pencils == 0:
            print(f"{current_player} won!")
            break
        current_player = name2 if current_player == name1 else name1

def stage3(pencils, first_player, name1, name2):
    """
    Основна функція для третього етапу.
    Додає контроль введення та визначає переможця.
    """
    current_player = first_player
    while pencils > 0:
        print_pencils(pencils)
        taken = take_pencils(current_player, pencils)
        pencils -= taken
        if pencils == 0:
            print(f"{current_player} won!")
            break
        current_player = name2 if current_player == name1 else name1

def bot_turn(pencils):
    """
    Визначає кількість олівців, яку візьме бот.

    Аргументи:
        pencils (int): Кількість олівців на столі.

    Повертає:
        int: Кількість взятих олівців.
    """
    if pencils % 4 == 0:
        return 3
    elif pencils % 4 == 3:
        return 2
    elif pencils % 4 == 2:
        return 1
    else:
        return random.randint(1, 3)


def stage4(pencils, first_player, name1, name2):
    """
    Основна функція для четвертого етапу.
    Реалізує гру з ботом, який дотримується виграшної стратегії.
    """
    current_player = first_player
    while pencils > 0:
        print_pencils(pencils)
        if current_player == name2:
            taken = bot_turn(pencils)
            print(f"{current_player}'s turn:\n{taken}")
        else:
            taken = take_pencils(current_player, pencils)
        pencils -= taken
        if pencils == 0:
            print(f"{current_player} won!")
            break
        current_player = name2 if current_player == name1 else name1

def main():
    pencils, first_player, name1, name2 = stage1()
    stage4(pencils, first_player, name1, name2)

if __name__ == "__main__":
    main()