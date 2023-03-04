import sys


class Wisielec:

    def __init__(self):
        self.found_indexes = None
        self.no_of_tries = 5
        self.word = "kamila"
        self.used_letters = []
        self.user_word = []

    @staticmethod
    def find_indexes(word, letter):
        indexes = []
        for index, letter_in_word in enumerate(word):
            if letter == letter_in_word:
                indexes.append(index)
        return indexes

    def show_state_of_game(self):
        print()
        print(self.user_word)
        print("Pozostało prób: ", self.no_of_tries)
        print("Użyte litery: ", self.used_letters)
        print()

    def main_wisielec(self):
        for _ in self.word:  # jeśli nie wykorzystujemy zmiennej w pętli tylko iterujemy się po niej możemy użyć _ zamiast nowej zmiennej
            self.user_word.append("_")

        while True:
            letter = input("Podaj literę: ")

            self.used_letters.append(letter)
            self.found_indexes = Wisielec.find_indexes(self.word, letter)

            if len(self.found_indexes) == 0:
                print("Nie ma takiej litery.")

                self.no_of_tries -= 1

                if self.no_of_tries == 0:
                    print("Koniec gry")
                    sys.exit(0)
            else:
                for index in self.found_indexes:
                    self.user_word[index] = letter
                if "".join(self.user_word) == self.word:
                    print("Brawo wygrałeś")
                    sys.exit(0)
            self.show_state_of_game()
