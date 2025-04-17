def print_help():
    """
    Виводить довідку про доступні команди форматування та спеціальні команди.

    Виводить:
        - Список доступних форматів
        - Список спеціальних команд (!help, !done)
    """
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")

def handle_header():
    """
    Обробляє створення заголовку Markdown.

    Запитує:
        - Рівень заголовку (1-6)
        - Текст заголовку

    Повертає:
        - Рядок із заголовком у форматі Markdown

    Виводить повідомлення про помилку, якщо рівень не в межах 1-6.
    """
    while True:
        level = input("Level: > ")
        if not level.isdigit() or int(level) < 1 or int(level) > 6:
            print("The level should be within the range of 1 to 6")
        else:
            text = input("Text: > ")
            return f"{'#' * int(level)} {text}\n"


def handle_link():
    """
    Обробляє створення посилання Markdown.

    Запитує:
        - Текст посилання (Label)
        - URL-адресу

    Повертає:
        - Рядок із посиланням у форматі Markdown
    """
    label = input("Label: > ")
    url = input("URL: > ")
    return f"[{label}]({url})"

def handle_list(ordered=False):
    """
    Обробляє створення впорядкованого або невпорядкованого списку Markdown.

    Параметри:
        - ordered: Чи є список впорядкованим (за замовчуванням False)

    Запитує:
        - Кількість елементів списку
        - Текст для кожного елементу списку

    Повертає:
        - Рядок із списком у форматі Markdown

    Виводить повідомлення про помилку, якщо кількість елементів <= 0.
    """
    while True:
        rows = input("Number of rows: > ")
        if not rows.isdigit() or int(rows) <= 0:
            print("The number of rows should be greater than zero")
        else:
            break

    items = []
    for i in range(1, int(rows) + 1):
        item = input(f"Row #{i}: > ")
        if ordered:
            items.append(f"{i}. {item}")
        else:
            items.append(f"* {item}")

    return '\n'.join(items) + '\n'

def main():
    """
    Головна функція програми Markdown-редактора.

    Логіка роботи:
    1. Виводить довідку при старті
    2. Запускає цикл обробки команд:
        - !help - виводить довідку
        - !done - зберігає результат у файл та завершує роботу
        - Інші команди - застосовує відповідне форматування
    3. Після кожного форматування виводить поточний стан розмітки
    4. При завершенні зберігає результат у файл output.md
    """
    markdown_content = []
    formatters = {
        'plain': lambda: input("Text: > "),
        'bold': lambda: f"**{input('Text: > ')}**",
        'italic': lambda: f"*{input('Text: > ')}*",
        'inline-code': lambda: f"`{input('Text: > ')}`",
        'header': handle_header,
        'link': handle_link,
        'new-line': lambda: '\n',
        'ordered-list': lambda: handle_list(ordered=True),
        'unordered-list': lambda: handle_list(ordered=False)
    }

    while True:
        user_input = input("Choose a formatter: > ")

        if user_input == '!help':
            print_help()
        elif user_input == '!done':
            with open('output.md', 'w') as f:
                f.write(''.join(markdown_content))
            break
        elif user_input in formatters:
            try:
                result = formatters[user_input]()
                markdown_content.append(result)
                print(''.join(markdown_content))
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    print_help()
    main()