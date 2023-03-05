import calendar
import datetime


class DzienUrodzin:

    @staticmethod
    def translate_to_polish(day_name):
        # od 3.10 pythona można używać match case odpowiednik switch case z javy prawie :)
        translate_dictionary = {
            "Monday": "Poniedziałek",
            "Tuesday": "Wtorek",
            "Wednesday": "Środa",
            "Thursday": "Czwartek",
            "Friday": "Piątek",
            "Saturday": "Sobota",
            "Sunday": "Niedziela"
        }
        return translate_dictionary[day_name]
        # if day_name == "Monday":
        #     return "Poniedziałek"
        # elif day_name == "Tuesday":
        #     return "Wtorek"
        # elif day_name == "Wednesday":
        #     return "Środa"
        # elif day_name == "Thursday":
        #     return "Czwartek"
        # elif day_name == "Saturday":
        #     return "Sobota"
        # elif day_name == "Sunday":
        #     return "Niedziela"

    def main_dzien_urodzin(self):
        date_of_birth = input("Podaj datę urodzin w formacie dzień-miesiąc-rok (np. 1-1-2000): ")
        day, month, year = date_of_birth.split("-")  # (1, 1, 2000)

        date_of_birth = datetime.datetime(int(year), int(month), int(day))

        day_name = calendar.day_name[date_of_birth.weekday()]
        print(DzienUrodzin.translate_to_polish(day_name))
