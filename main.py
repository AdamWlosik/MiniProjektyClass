from AvatarGenerator.AvatarGenerator import AvatarGenerator
from CitiesSQL.CitiesSQL import CitiesSQL
from DzieńUrodzin.DayOfBirth import DayOfBirth
from GeneratorHaselKomenda.CommendPasswordGenerator import CommendPasswordGenerator
from GeneratorHaseł.PasswordGenerator import PasswordGenerator
from Quiz.Quiz import Quiz
from SledzenieWydatków.ExpenseTrack import ExpenseTrack
from ToDoListSQLlite.ToDoListSQLlite import ToDoListSQLlite
from Wisielec.Hangman import Hangman

print()
print("Aby uruchomić wybierz numer projektu, funkcje main w klasach będą edytowane w przyszłości")
print()
print("1. Uruchom projekt Wisielec")
print("2. Uruchom projekt GeneratorHaseł")
print("3. Uruchom projekt GeneratorHasełKomenda")
print("4. Uruchom projekt Quiz")
print("5. Uruchom projekt ŚledzenieWydatków")
print("6. Uruchom projekt ToDoListSQLlite ")
print("7. Uruchom projekt DzieńUrodzin")
print("8. Uruchom projekt AvatarGenerator")
print("9. Uruchom projekt CitiesSQL")

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

elif menu == 8:
    AvatarGenerator().avatar_generator()

elif menu == 9:
    CitiesSQL().cities_main()