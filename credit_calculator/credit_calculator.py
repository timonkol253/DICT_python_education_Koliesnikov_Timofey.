import math
import argparse


def calculate_num_payments(principal, payment):
    """
    Обчислює кількість платежів для погашення кредиту та останній платіж.

    Args:
        principal (int): Сума кредиту.
        payment (int): Щомісячний платіж.
    """
    months = principal // payment
    last_payment = principal % payment

    if last_payment != 0:
        months += 1
        print(f"It will take {months - 1} months to repay the loan")
        print(f"The last payment will be {last_payment}")
    else:
        print(f"It will take {months} months to repay the loan")


def calculate_monthly_payment(principal, months):
    """
    Обчислює суму щомісячного платежу.

    Args:
        principal (int): Сума кредиту.
        months (int): Кількість платежів.
    """
    payment = principal // months
    last_payment = principal % months

    if last_payment != 0:
        payment += 1
        last_payment = principal - (payment * (months - 1))
        print(f"Your monthly payment = {payment} and the last payment = {last_payment}")
    else:
        print(f"Your monthly payment = {payment}")


def calculate_annuity_payment(principal, periods, interest):
    """
    Обчислює ануїтетний платіж.

    Args:
        principal (int): Сума кредиту.
        periods (int): Кількість платежів.
        interest (float): Відсоткова ставка.

    Returns:
        int: Ануїтетний платіж.
    """
    i = interest / (12 * 100)
    payment = principal * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1)
    return math.ceil(payment)


def calculate_loan_principal(payment, periods, interest):
    """
    Обчислює основну суму кредиту.

    Args:
        payment (float): Щомісячний платіж.
        periods (int): Кількість платежів.
        interest (float): Відсоткова ставка.

    Returns:
        int: Основна сума кредиту.
    """
    i = interest / (12 * 100)
    principal = payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
    return int(principal)


def calculate_periods(principal, payment, interest):
    """
    Обчислює кількість платежів.

    Args:
        principal (int): Сума кредиту.
        payment (float): Щомісячний платіж.
        interest (float): Відсоткова ставка.
    """
    i = interest / (12 * 100)
    periods = math.log(payment / (payment - i * principal)) / math.log(1 + i)
    periods = math.ceil(periods)

    years = periods // 12
    months = periods % 12

    if years > 0 and months > 0:
        print(f"It will take {years} years and {months} months to repay this loan!")
    elif years > 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {months} months to repay this loan!")


def calculate_diff_payments(principal, periods, interest):
    """
    Обчислює диференційовані платежі та переплату.

    Args:
        principal (int): Сума кредиту.
        periods (int): Кількість платежів.
        interest (float): Відсоткова ставка.
    """
    i = interest / (12 * 100)
    total_payment = 0

    for month in range(1, periods + 1):
        diff_payment = math.ceil(
            (principal / periods) + i * (principal - (principal * (month - 1)) / periods)
        )
        print(f"Month {month}: payment is {diff_payment}")
        total_payment += diff_payment

    overpayment = total_payment - principal
    print(f"Overpayment = {overpayment}")


def display_loan_info():
    """
    Виводить статичну інформацію про погашення кредиту.
    """
    print("Loan principal: 1000")
    print("Month 1: repaid 250")
    print("Month 2: repaid 250")
    print("Month 3: repaid 500")
    print("The loan has been repaid!")


def handle_user_input():
    """
    Обробляє введення користувача для розрахунку кількості платежів або суми платежу.
    """
    principal = int(input("Enter the loan principal:\n"))

    print("""What do you want to calculate?
type "m" – for number of monthly payments,
type "p" – for the monthly payment:""")
    option = input()

    if option == "m":
        payment = int(input("Enter the monthly payment:\n"))
        calculate_num_payments(principal, payment)
    elif option == "p":
        months = int(input("Enter the number of months:\n"))
        calculate_monthly_payment(principal, months)


def handle_annuity_calculation():
    """
    Обробляє розрахунок ануїтетного платежу, основної суми або кількості платежів.
    """
    print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
    option = input()

    if option == "n":
        principal = int(input("Enter the loan principal:\n"))
        payment = float(input("Enter the monthly payment:\n"))
        interest = float(input("Enter the loan interest:\n"))
        calculate_periods(principal, payment, interest)

    elif option == "a":
        principal = int(input("Enter the loan principal:\n"))
        periods = int(input("Enter the number of periods:\n"))
        interest = float(input("Enter the loan interest:\n"))
        payment = calculate_annuity_payment(principal, periods, interest)
        print(f"Your monthly payment = {payment}!")

    elif option == "p":
        payment = float(input("Enter the annuity payment:\n"))
        periods = int(input("Enter the number of periods:\n"))
        interest = float(input("Enter the loan interest:\n"))
        principal = calculate_loan_principal(payment, periods, interest)
        print(f"Your loan principal = {principal}!")


def handle_command_line_arguments():
    """
    Обробляє аргументи командного рядка для розрахунку кредиту з використанням argparse.
    """
    parser = argparse.ArgumentParser(description="Loan calculator")

    # Required arguments
    parser.add_argument("--type", choices=["annuity", "diff"],
                        help="Type of payment: 'annuity' or 'diff'")
    parser.add_argument("--principal", type=int,
                        help="Loan principal amount")
    parser.add_argument("--periods", type=int,
                        help="Number of payment periods (months)")
    parser.add_argument("--interest", type=float,
                        help="Annual interest rate (without percent sign)")
    parser.add_argument("--payment", type=float,
                        help="Monthly payment amount (for annuity only)")

    args = parser.parse_args()

    if args.type is None or args.interest is None:
        print("Incorrect parameters")
        return

    if args.type == "diff" and args.payment is not None:
        print("Incorrect parameters (diff payment doesn't support --payment)")
        return

    if args.type == "annuity":
        if args.principal is None and args.payment is None:
            print("Incorrect parameters (need either principal or payment)")
            return
        if args.periods is None and (args.principal is None or args.payment is None):
            print("Incorrect parameters (need periods or both principal and payment)")
            return

    if args.type == "diff":
        if args.principal is not None and args.periods is not None:
            calculate_diff_payments(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters (need principal and periods for diff)")

    elif args.type == "annuity":
        if args.principal is None:
            principal = calculate_loan_principal(args.payment, args.periods, args.interest)
            print(f"Your loan principal = {principal}!")
        elif args.payment is None:
            payment = calculate_annuity_payment(args.principal, args.periods, args.interest)
            print(f"Your monthly payment = {payment}!")
        elif args.periods is None:
            calculate_periods(args.principal, args.payment, args.interest)


def main():
    print("""Select the mode:
1 - Display loan info
2 - User input calculation
3 - Annuity calculation
4 - Command line calculation""")

    choice = input()

    if choice == "1":
        display_loan_info()
    elif choice == "2":
        handle_user_input()
    elif choice == "3":
        handle_annuity_calculation()
    elif choice == "4":
        handle_command_line_arguments()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()