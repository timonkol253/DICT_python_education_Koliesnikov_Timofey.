import random  # Импортируем модуль для случайного выбора слова

WORDS = ['python', 'java', 'javascript', 'php']  # Список слов для игры
MAX_ERRORS = 8  # Максимальное количество ошибок, допустимых в игре

def greet():
    # Приветствует игрока и выводит название игры
    print("HANGMAN")
    print("The game will be available soon.")

def choose_word():
    # Выбирает случайное слово из списка WORDS
    return random.choice(WORDS)

def display_hint(word):
    # Выводит подсказку: первые три буквы слова и затем дефисы
    hint = word[:3] + '-' * (len(word) - 3)
    print(f"Guess the word {hint}: ")

def get_valid_letter(guessed_letters):
    # Запрашивает у пользователя букву и проверяет корректность ввода
    while True:
        letter = input("Input a letter: ").lower()

        if len(letter) != 1:
            print("You should input a single letter")  # Проверка: одна буква
        elif not letter.isalpha() or not letter.islower():
            print("Please enter a lowercase English letter")  # Проверка: строчная английская буква
        elif letter in guessed_letters:
            print("You've already guessed this letter")  # Проверка: не угаданная ранее буква
        else:
            return letter  # Возвращает букву, если она прошла все проверки

def play_game():
    # Основная логика игры "Виселица"
    word = choose_word()  # Выбираем случайное слово
    guessed_letters = set()  # Множество угаданных букв
    display_word = '-' * len(word)  # Отображаемое слово с дефисами вместо букв
    errors = 0  # Счетчик ошибок

    print(display_word)  # Печатаем начальное состояние слова

    while errors < MAX_ERRORS and '-' in display_word:
        letter = get_valid_letter(guessed_letters)  # Получаем допустимую букву
        guessed_letters.add(letter)  # Добавляем букву в угаданные

        if letter in word:
            # Обновляем отображаемое слово, если буква есть в загаданном слове
            display_word = ''.join([letter if word[i] == letter else display_word[i] for i in range(len(word))])
            print(display_word)
        else:
            print("That letter doesn't appear in the word")  # Сообщение, если буква не угадана
            errors += 1  # Увеличиваем счетчик ошибок

        print(f"Attempts remaining: {MAX_ERRORS - errors}")  # Количество оставшихся попыток

    if '-' not in display_word:
        print(f"You guessed the word {word}!")  # Сообщение о победе
        print("You survived!")
    else:
        print("You lost!")  # Сообщение о поражении

def main_menu():
    # Главное меню, где пользователь выбирает "играть" или "выйти"
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: ').strip().lower()

        if choice == "play":
            play_game()  # Начинаем игру
        elif choice == "exit":
            print("Thanks for playing!")  # Выход из игры
            break
        else:
            print("Invalid choice. Please type 'play' or 'exit'.")  # Проверка выбора

if __name__ == "__main__":
    greet()  # Приветствие при запуске
    main_menu()  # Запуск главного меню
