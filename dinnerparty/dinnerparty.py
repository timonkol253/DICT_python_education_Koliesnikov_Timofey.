import random

# Этап 1: Добавление друзей
def add_friends():
    """
    Считывает количество участников и их имена, затем возвращает словарь с именами друзей и их текущими балансами (нулевыми).

    Returns:
        dict: Словарь, где ключи — имена друзей, значения — их баланс (изначально 0).
        None: Возвращается, если количество участников введено неверно или равно нулю.
    """
    print("Enter the number of friends joining (including you):")
    num_friends = input().strip()

    if not num_friends.isdigit() or int(num_friends) <= 0:
        print("No one is joining for the party")
        return None

    num_friends = int(num_friends)
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(num_friends):
        name = input("> ").strip()
        while not name or name in friends:  # Проверка на уникальность имен и пустой ввод
            print(f"{name} is already in the list or invalid. Enter another name:")
            name = input("> ").strip()
        friends[name] = 0
    return friends

# Этап 2: Разделение суммы
def split_bill(friends):
    """
    Делит введенную сумму на всех участников и обновляет их баланс.

    Args:
        friends (dict): Словарь с именами участников и их текущими балансами.

    Returns:
        float: Общая сумма, введенная пользователем.
        None: Если ввод суммы некорректный.
    """
    print("Enter the total amount:")
    total_amount = input().strip()

    # Проверка на корректный ввод числа с одной точкой
    if not total_amount.replace('.', '', 1).isdigit() or total_amount.count('.') > 1:
        print("Invalid input")
        return None

    total_amount = float(total_amount)
    split_amount = round(total_amount / len(friends), 2)
    remainder = round(total_amount - split_amount * len(friends), 2)

    for i, friend in enumerate(friends):
        friends[friend] = split_amount
        if i < int(remainder * 100):  # Распределяем остаток
            friends[friend] += 0.01
    return total_amount

# Этап 3: Выбор "счастливчика"
def choose_lucky(friends):
    """
    Случайным образом выбирает одного "счастливчика", который не будет участвовать в оплате.

    Args:
        friends (dict): Словарь с именами участников и их текущими балансами.

    Returns:
        str: Имя выбранного "счастливчика".
        None: Если пользователь отказывается использовать функцию.
    """
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    use_lucky = input().strip()

    if use_lucky.lower() == "yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")
        return lucky_one
    else:
        print("No one is going to be lucky")
        return None

# Этап 4: Перерасчет суммы
def recalculate_bill(friends, total_amount, lucky_one):
    """
    Перерасчитывает суммы, учитывая, что "счастливчик" не участвует в оплате.

    Args:
        friends (dict): Словарь с именами участников и их текущими балансами.
        total_amount (float): Общая сумма для распределения.
        lucky_one (str): Имя "счастливчика", освобожденного от оплаты.

    Returns:
        None
    """
    if lucky_one:
        split_amount = round(total_amount / (len(friends) - 1), 2)
        for friend in friends:
            friends[friend] = split_amount if friend != lucky_one else 0
    print(friends)

# Основная программа
if __name__ == "__main__":
    friends = add_friends()
    if friends:
        total_amount = split_bill(friends)
        if total_amount is not None:
            lucky_friend = choose_lucky(friends)
            recalculate_bill(friends, total_amount, lucky_friend)
