class SledzenieWydatkow:

    def __init__(self):
        self.expenses = []

    def show_expenses(self, month):
        for expense_amount, expense_type, expense_month in self.expenses:
            if expense_month == month:
                print(f'{expense_amount} - {expense_type}')

    def add_expense(self, month):
        print()
        expense_amount = int(input("Podaj kwotę [zł]: "))
        expense_type = input("Podaj typ wydatku: ")

        expense = (expense_amount, expense_type, month)
        self.expenses.append(expense)

    def show_stats(self, month):
        total_amount_this_mount = sum(expense_amount for expense_amount, _, expense_month in self.expenses
                                      if expense_month == month)
        total_amount_all = sum(expense_amount for expense_amount, _, _ in self.expenses)
        number_of_expanse_this_month = sum(1 for _, _, expense_month in self.expenses if expense_month == month)
        average_expense_this_month = total_amount_this_mount / number_of_expanse_this_month
        average_expense_all = total_amount_all / len(self.expenses)

        print()
        print("Statystyki:")
        print("Wszystkie wydatki w tym miesiącu: ", total_amount_this_mount)
        print("Wszystkie wydatki: ", total_amount_all)
        print("Średni wydatek w tym miesiącu", average_expense_this_month)
        print("Średni wydatek: ", average_expense_all)

    def main_sledzenie_wydatkow(self):
        while True:
            print()
            month = int(input("Wybierz miesiąc [1-12]: "))

            if month == 0:
                break

            while True:
                print()
                print("0. Powrót do wyboru miesiąca")
                print("1. Wyświetl wszystkie wydatki")
                print("2. Dodaj wydatek")
                print("3. Statystyki")
                choice = int(input("Wybierz opcje: "))

                if choice == 0:
                    break

                if choice == 1:
                    SledzenieWydatkow.show_expenses(self, month)

                if choice == 2:
                    SledzenieWydatkow.add_expense(self, month)

                if choice == 3:
                    SledzenieWydatkow.show_stats(self, month)
