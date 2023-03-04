from GeneratorHaselKomenda.GeneratorHaselKomenda import GeneratorHaselKomenda
from GeneratorHaseł.GeneratorHasel import GeneratorHasel
from Quiz.Quiz import Quiz
from SledzenieWydatków.SledzenieWydatków import SledzenieWydatkow
from ToDoListSQLlite.ToDoListSQLlite import ToDoListSQLlite
from Wisielec.Wisielec import Wisielec

print("1. Uruchom projekt Wisielec")
print("2. Uruchom projekt GeneratorHaseł")
print("3. Uruchom projekt GeneratorHasełKomenda")
print("4. Uruchom projekt Quiz")
print("5. Uruchom projekt ŚledzenieWydatków")
print("6. Uruchom projekt ToDoListSQLlite ")

menu = int(input("Wybierz projekt: "))
if menu == 1:
    Wisielec().main_wisielec()

elif menu == 2:
    GeneratorHasel().main_generator_hasel()

elif menu == 3:
    GeneratorHaselKomenda().main_generator_hasel_komenda()

elif menu == 4:
    Quiz().quiz_main()

elif menu == 5:
    SledzenieWydatkow().main_sledzenie_wydatkow()

elif menu == 6:
    ToDoListSQLlite().to_do_list_sql_lile_main()
