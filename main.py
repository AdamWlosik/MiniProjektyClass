from DzieńUrodzin.DayOfBirth import DayOfBirth
from GeneratorHaselKomenda.CommendPasswordGenerator import CommendPasswordGenerator
from GeneratorHaseł.PasswordGenerator import PasswordGenerator
from Quiz.Quiz import Quiz
from SledzenieWydatków.ExpenseTrack import ExpenseTrack
from ToDoListSQLlite.ToDoListSQLlite import ToDoListSQLlite
from Wisielec.Hangman import Hangman

print("1. Uruchom projekt Wisielec")
print("2. Uruchom projekt GeneratorHaseł")
print("3. Uruchom projekt GeneratorHasełKomenda")
print("4. Uruchom projekt Quiz")
print("5. Uruchom projekt ŚledzenieWydatków")
print("6. Uruchom projekt ToDoListSQLlite ")
print("7. Uruchom projekt DzieńUrodzin")

menu = int(input("Wybierz projekt: "))
if menu == 1:
    Hangman().main_wisielec()

elif menu == 2:
    PasswordGenerator().main_generator_hasel()

elif menu == 3:
    CommendPasswordGenerator().main_generator_hasel_komenda()

elif menu == 4:
    Quiz().quiz_main()

elif menu == 5:
    ExpenseTrack().main_sledzenie_wydatkow()

elif menu == 6:
    ToDoListSQLlite().to_do_list_sql_lile_main()

elif menu == 7:
    DayOfBirth().main_dzien_urodzin()
