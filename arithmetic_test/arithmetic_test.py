import random
import os

def generate_level1_question():
    """Генерує просте арифметичне завдання (числа від 2 до 9, операції +, -, *)"""
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    op = random.choice(['+', '-', '*'])
    question = f"{a} {op} {b}"
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    else:  # op == '*'
        answer = a * b
    return question, answer


def simple_arithmetic_test():
    """Тестування з першого етапу - одне завдання з перевіркою відповіді"""
    question, answer = generate_level1_question()
    print(question)
    user_input = input("> ")
    try:
        user_answer = int(user_input)
        print("Right!" if user_answer == answer else "Wrong!")
    except ValueError:
        print("Wrong!")

def get_valid_answer():
    """Отримує коректну числову відповідь від користувача з обробкою помилок"""
    while True:
        user_input = input("> ").strip()
        if not user_input or not user_input.lstrip('-').isdigit():
            print("Incorrect format.")
            continue
        return int(user_input)


def five_questions_test():
    """Проводить тест з 5 завдань, підраховує та виводить результат"""
    correct = 0
    for _ in range(5):
        question, answer = generate_level1_question()
        print(question)

        user_answer = get_valid_answer()

        if user_answer == answer:
            print("Right!")
            correct += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct}/5.")


def generate_level2_question():
    """Генерує завдання для рівня 2 (квадрати чисел від 11 до 29)"""
    num = random.randint(11, 29)
    return str(num), num ** 2


def select_level():
    """Запитує у користувача рівень складності з перевіркою вводу"""
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        level = input("> ").strip()
        if level in ['1', '2']:
            return int(level)
        print("Incorrect format.")

def run_selected_level(level):
    """Запускає тест для обраного рівня складності"""
    correct = 0
    for _ in range(5):
        if level == 1:
            question, answer = generate_level1_question()
        else:
            question, answer = generate_level2_question()

        print(question)
        user_answer = get_valid_answer()

        if user_answer == answer:
            print("Right!")
            correct += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct}/5.")
    return correct


def save_results(correct, level):
    """Зберігає результати тесту у файл results.txt"""
    level_desc = ("simple operations with numbers 2-9" if level == 1
                  else "integral squares of 11-29")
    name = input("What is your name?\n> ").strip()
    result = f"{name}: {correct}/5 in level {level} ({level_desc})."

    with open("results.txt", "a") as f:
        f.write(result + "\n")
    print('The results are saved in "results.txt".')


def advanced_test():
    """Головна функція для третього етапу (вибір рівня, тест, збереження)"""
    level = select_level()
    correct = run_selected_level(level)

    while True:
        choice = input('Would you like to save your result to the file? Enter yes or no.\n> ').lower()
        if choice in ['yes', 'y']:
            save_results(correct, level)
            break
        elif choice in ['no', 'n']:
            break
        print("Please enter yes or no.")

if __name__ == "__main__":
    advanced_test()