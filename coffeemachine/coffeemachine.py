class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
        self.state = "main" #Начальное состаяние

    def process_action(self, action):
        """
        Обробляє введену дію в залежності від поточного стану кавоварки.
        Якщо дія не відповідає поточному стану, виводиться помилка.
        """
        if self.state == "main":
            if action == "buy":
                self.state = "choose_coffee"
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.show_remaining()
            elif action == "exit":
                exit()
            else:
                print("Invalid action, please try again.")

        elif self.state == "choose_coffee":
            if action == "1":
                self.buy_coffee("espresso")
            elif action == "2":
                self.buy_coffee("latte")
            elif action == "3":
                self.buy_coffee("cappuccino")
            elif action == "back":
                self.state = "main"
                print("Back to main menu.")
            else:
                print("Invalid selection, please try again.")

    def buy_coffee(self, coffee_type):
        """
        Купує каву, перевіряючи наявність необхідних ресурсів.
        Якщо ресурсів не вистачає, виводиться відповідне повідомлення.
        """
        if coffee_type == "espresso":
            required_water = 250
            required_milk = 0
            required_beans = 16
            price = 4
        elif coffee_type == "latte":
            required_water = 350
            required_milk = 75
            required_beans = 20
            price = 7
        elif coffee_type == "cappuccino":
            required_water = 200
            required_milk = 100
            required_beans = 12
            price = 6

        # Перевірка наявності всіх ресурсів
        if self.water >= required_water and self.milk >= required_milk and self.coffee_beans >= required_beans and self.cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.water -= required_water
            self.milk -= required_milk
            self.coffee_beans -= required_beans
            self.cups -= 1
            self.money += price
            self.state = "main"  # Повертаємось в головне меню після покупки
        else:
            print(f"Sorry, not enough resources to make {coffee_type}!")

    def fill(self):
        """
        Додає ресурси (воду, молоко, кавові зерна та чашки) до кавоварки.
        """
        self.water += int(input("Write how many ml of water you want to add: "))
        self.milk += int(input("Write how many ml of milk you want to add: "))
        self.coffee_beans += int(input("Write how many grams of coffee beans you want to add: "))
        self.cups += int(input("Write how many disposable cups of coffee you want to add: "))

    def take(self):
        """
        Виводить кількість грошей, які є в кавоварці, і обнуляє її.
        """
        print(f"I gave you {self.money}")
        self.money = 0

    def show_remaining(self):
        """
        Виводить інформацію про поточні ресурси кавоварки.
        """
        print(
            f"The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.coffee_beans} of coffee beans\n{self.cups} of disposable cups\n{self.money} of money")

# Створення об'єкта кавоварки
coffee_machine = CoffeeMachine()

# Основний цикл програми
while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")
    coffee_machine.process_action(action)

